'''
Function:
    Implementation of Trainer
Author:
    Zhenchao Jin
'''
import os
import copy
import torch
import warnings
import argparse
import torch.distributed as dist
from modules import BuildRunner, ConfigParser
warnings.filterwarnings('ignore')


'''parsecmdargs'''
def parsecmdargs():
    parser = argparse.ArgumentParser(description='CSSegmentation: An Open Source Continual Semantic Segmentation Toolbox Based on PyTorch.')
    parser.add_argument('--local_rank', '--local-rank', dest='local_rank', help='node rank for distributed training.', default=0, type=int)
    parser.add_argument('--nproc_per_node', dest='nproc_per_node', help='number of processes per node.', default=4, type=int)
    parser.add_argument('--cfgfilepath', dest='cfgfilepath', help='config file path you want to load.', type=str, required=True)
    parser.add_argument('--starttaskid', dest='starttaskid', help='task id you want to start from.', default=0, type=int)
    cmd_args = parser.parse_args()
    if torch.__version__.startswith('2.'):
        cmd_args.local_rank = int(os.environ['LOCAL_RANK'])
    return cmd_args


'''Trainer'''
class Trainer():
    def __init__(self, cmd_args):
        self.cmd_args = cmd_args
        config_parser = ConfigParser()
        self.cfg, _ = config_parser(cmd_args.cfgfilepath)
    '''start'''
    def start(self):
        # initialize
        assert torch.cuda.is_available(), 'cuda is not available'
        cmd_args, runner_cfg = self.cmd_args, self.cfg.RUNNER_CFG
        dist.init_process_group(backend=runner_cfg['parallel_cfg']['backend'], init_method=runner_cfg['parallel_cfg']['init_method'])
        torch.cuda.set_device(cmd_args.local_rank)
        torch.backends.cudnn.allow_tf32 = False
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.benchmark = runner_cfg['benchmark']
        # iter tasks
        for task_id in range(cmd_args.starttaskid, runner_cfg['num_tasks']):
            runner_cfg_task = copy.deepcopy(runner_cfg)
            runner_cfg_task['task_id'] = task_id
            for key in ['segmentor_cfg', 'dataset_cfg', 'dataloader_cfg', 'scheduler_cfg', 'parallel_cfg']:
                if isinstance(runner_cfg_task[key], list):
                    assert len(runner_cfg_task[key]) == runner_cfg_task['num_tasks']
                    runner_cfg_task[key] = runner_cfg_task[key][task_id]
            runner_client = BuildRunner(mode='TRAIN', cmd_args=cmd_args, runner_cfg=runner_cfg_task)
            runner_client.start()


'''main'''
if __name__ == '__main__':
    cmd_args = parsecmdargs()
    trainer_client = Trainer(cmd_args=cmd_args)
    trainer_client.start()