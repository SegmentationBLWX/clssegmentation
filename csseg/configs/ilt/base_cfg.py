'''BASE_CFG for ILT'''
# SEGMENTOR_CFG
SEGMENTOR_CFG = {
    'type': 'ILTSegmentor',
    'num_known_classes_list': None,
    'selected_indices': (0,), 
    'align_corners': False, 
    'encoder_cfg': {
        'type': 'ResNetILT',
        'depth': 101,
        'outstride': 16,
        'out_indices': (3,),
        'norm_cfg': {'type': 'InPlaceABNSync', 'activation': 'leaky_relu', 'activation_param': 0.01},
        'act_cfg': None,
        'shortcut_norm_cfg': {'type': 'InPlaceABNSync', 'activation': 'identity'},
        'shortcut_act_cfg': {'type': 'LeakyReLU', 'inplace': True, 'negative_slope': 0.01},
        'pretrained': True,
        'structure_type': 'resnet101inplaceabn',
    }, 
    'decoder_cfg': {
        'type': 'ASPPHead',
        'in_channels': 2048,
        'feats_channels': 256,
        'out_channels': 256,
        'dilations': (1, 6, 12, 18),
        'pooling_size': 32,
        'norm_cfg': {'type': 'InPlaceABNSync', 'activation': 'leaky_relu', 'activation_param': 0.01},
        'act_cfg': None,
    },
    'losses_cfgs': {
        'segmentation_init': {
            'loss_seg': {'CrossEntropyLoss': {'scale_factor': 1.0, 'reduction': 'mean', 'ignore_index': 255}}
        },
        'segmentation_cl' : {
            'loss_seg': {'CrossEntropyLoss': {'scale_factor': 1.0, 'reduction': 'mean', 'ignore_index': 255}}
        },
        'distillation_logits': {'scale_factor': 100, 'alpha': 1.0},
        'distillation_features': {'type': 'MSELoss', 'scale_factor': 100, 'reduction': 'mean'},
    },
}
# RUNNER_CFG
RUNNER_CFG = {
    'type': 'ILTRunner',
    'algorithm': 'ILT',
    'task_name': '',
    'task_id': -1,
    'num_tasks': -1,
    'work_dir': '',
    'benchmark': True,
    'save_interval_epochs': 10,
    'eval_interval_epochs': 10,
    'log_interval_iterations': 10,
    'choose_best_segmentor_by_metric': 'mean_iou',
    'logger_handle_cfg': {'type': 'LocalLoggerHandle', 'logfilepath': ''},
    'num_total_classes': -1,
    'fp16_cfg': {'type': 'pytorch', 'autocast': {}, 'grad_scaler': {}},
    'segmentor_cfg': SEGMENTOR_CFG,
}