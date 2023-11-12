'''ilt_r101iabnd16_aspp_512x512_vocaug10-1_overlap'''
import os
from .base_cfg import RUNNER_CFG
from .._base_ import DATASET_CFG_VOCAUG_512x512, SCHEDULER_CFG_POLY, DATALOADER_CFG_BS24, PARALLEL_CFG


# add dataset_cfg
RUNNER_CFG['dataset_cfg'] = DATASET_CFG_VOCAUG_512x512.copy()
RUNNER_CFG['dataset_cfg']['overlap'] = True
# add dataloader_cfg
RUNNER_CFG['dataloader_cfg'] = DATALOADER_CFG_BS24.copy()
# add scheduler_cfg
RUNNER_CFG['scheduler_cfg'] = [
    SCHEDULER_CFG_POLY.copy() for _ in range(11)
]
RUNNER_CFG['scheduler_cfg'][0]['max_epochs'] = 30
RUNNER_CFG['scheduler_cfg'][0]['lr'] = 0.01
for i in range(1, 11):
    RUNNER_CFG['scheduler_cfg'][i]['max_epochs'] = 10
    RUNNER_CFG['scheduler_cfg'][i]['lr'] = 0.001
# add parallel_cfg
RUNNER_CFG['parallel_cfg'] = PARALLEL_CFG.copy()
# modify RUNNER_CFG
RUNNER_CFG.update({
    'task_name': '10-1',
    'num_tasks': 11,
    'num_total_classes': 21,
    'work_dir': os.path.split(__file__)[-1].split('.')[0],
    'logfilepath': f"{os.path.split(__file__)[-1].split('.')[0]}/{os.path.split(__file__)[-1].split('.')[0]}.log",
})