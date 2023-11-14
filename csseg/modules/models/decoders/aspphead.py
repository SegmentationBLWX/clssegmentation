'''
Function:
    Implementation of ASPPHead
Author:
    Zhenchao Jin
'''
import torch
import torch.nn as nn
import torch.nn.functional as F
from ..encoders import BuildNormalization, BuildActivation


'''ASPPHead'''
class ASPPHead(nn.Module):
    def __init__(self, in_channels, feats_channels, out_channels, dilations, pooling_size=32, norm_cfg=None, act_cfg=None):
        super(ASPPHead, self).__init__()
        # set attributes
        self.in_channels = in_channels
        self.feats_channels = feats_channels
        self.out_channels = out_channels
        self.dilations = dilations
        self.pooling_size = (pooling_size, pooling_size) if isinstance(pooling_size, int) else pooling_size
        self.norm_cfg = norm_cfg
        self.act_cfg = act_cfg
        # parallel convolutions
        self.parallel_convs = nn.ModuleList()
        for _, dilation in enumerate(dilations):
            if dilation == 1:
                conv = nn.Conv2d(in_channels, feats_channels, kernel_size=1, stride=1, padding=0, dilation=dilation, bias=False)
            else:
                conv = nn.Conv2d(in_channels, feats_channels, kernel_size=3, stride=1, padding=dilation, dilation=dilation, bias=False)
            self.parallel_convs.append(conv)
        self.parallel_bn = BuildNormalization(placeholder=feats_channels * len(dilations), norm_cfg=norm_cfg)
        self.parallel_act = BuildActivation(act_cfg)
        # global branch
        self.global_branch = nn.Sequential(
            nn.Conv2d(in_channels, feats_channels, kernel_size=1, stride=1, padding=0, bias=False),
            BuildNormalization(placeholder=feats_channels, norm_cfg=norm_cfg),
            BuildActivation(act_cfg),
            nn.Conv2d(feats_channels, feats_channels, kernel_size=1, stride=1, padding=0, bias=False),
        )
        # output project
        self.out_project = nn.Sequential(
            nn.Conv2d(feats_channels * len(dilations), out_channels, kernel_size=1, stride=1, padding=0, bias=False),
            BuildNormalization(placeholder=out_channels, norm_cfg=norm_cfg),
            BuildActivation(act_cfg),
        )
    '''forward'''
    def forward(self, x):
        # feed to parallel convolutions
        outputs = torch.cat([conv(x) for conv in self.parallel_convs], dim=1)
        outputs = self.parallel_bn(outputs)
        outputs = self.parallel_act(outputs)
        outputs = self.out_project[0](outputs)
        # feed to global branch
        global_feats = self.globalpooling(x)
        global_feats = self.global_branch(global_feats)
        if self.training or self.pooling_size is None:
            global_feats = global_feats.repeat(1, 1, x.size(2), x.size(3))
        # shortcut
        outputs = outputs + global_feats
        outputs = self.out_project[1:](outputs)
        # return
        return outputs
    '''globalpooling'''
    def globalpooling(self, x):
        if self.training or self.pooling_size is None:
            global_feats = x.view(x.size(0), x.size(1), -1).mean(dim=-1)
            global_feats = global_feats.view(x.size(0), x.size(1), 1, 1)
        else:
            pooling_size = (min(self.pooling_size[0], x.shape[2]), min(self.pooling_size[1], x.shape[3]))
            padding = (
                (pooling_size[1] - 1) // 2, (pooling_size[1] - 1) // 2 if pooling_size[1] % 2 == 1 else (pooling_size[1] - 1) // 2 + 1,
                (pooling_size[0] - 1) // 2, (pooling_size[0] - 1) // 2 if pooling_size[0] % 2 == 1 else (pooling_size[0] - 1) // 2 + 1,
            )
            global_feats = F.avg_pool2d(x, pooling_size, stride=1)
            global_feats = F.pad(global_feats, pad=padding, mode='replicate')
        return global_feats