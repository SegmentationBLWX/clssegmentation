'''
Function:
    Implementation of VOCDataset
Author:
    Zhenchao Jin
'''
import os
import pandas as pd
from .base import _BaseDataset, BaseDataset


'''_VOCDataset'''
class _VOCDataset(_BaseDataset):
    num_classes = 21
    classnames = [
        '__background__', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
        'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
        'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]
    assert num_classes == len(classnames)
    def __init__(self, mode, dataset_cfg):
        super(_VOCDataset, self).__init__(mode, dataset_cfg)
        # set directory
        rootdir = dataset_cfg['rootdir']
        self.image_dir = os.path.join(rootdir, 'JPEGImages')
        self.ann_dir = os.path.join(rootdir, 'SegmentationClass')
        # obatin imageids
        set_dir = os.path.join(rootdir, 'ImageSets', 'Segmentation')
        df = pd.read_csv(os.path.join(set_dir, dataset_cfg['set']+'.txt'), names=['imageids'])
        self.imageids = df['imageids'].values
        self.imageids = [str(_id) for _id in self.imageids]


'''VOCDataset'''
class VOCDataset(BaseDataset):
    tasks = {
        'offline': {
            0: list(range(21)),
        },
        '19-1': {
            0: list(range(20)), 1: [20],
        },
        '15-5': {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            1: [16, 17, 18, 19, 20]
        },
        '15-5s': {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            1: [16], 2: [17], 3: [18], 4: [19], 5: [20]
        },
        '15-5s_b': {
            0: [0, 12, 9, 20, 7, 15, 8, 14, 16, 5, 19, 4, 1, 13, 2, 11],
            1: [17], 2: [3], 3: [6], 4: [18], 5: [10]
        },
        '15-5s_c': {
            0: [0, 13, 19, 15, 17, 9, 8, 5, 20, 4, 3, 10, 11, 18, 16, 7],
            1: [12], 2: [14], 3: [6], 4: [1], 5: [2]
        },
        '15-5s_d': {
            0: [0, 15, 3, 2, 12, 14, 18, 20, 16, 11, 1, 19, 8, 10, 7, 17],
            1: [6], 2: [5], 3: [13], 4: [9], 5: [4]
        },
        '15-5s_e': {
            0: [0, 7, 5, 3, 9, 13, 12, 14, 19, 10, 2, 1, 4, 16, 8, 17],
            1: [15], 2: [18], 3: [6], 4: [11], 5: [20]
        },
        '15-5s_f': {
            0: [0, 7, 13, 5, 11, 9, 2, 15, 12, 14, 3, 20, 1, 16, 4, 18],
            1: [8], 2: [6], 3: [10], 4: [19], 5: [17]
        },
        '15-5s_g': {
            0: [0, 7, 5, 9, 1, 15, 18, 14, 3, 20, 10, 4, 19, 11, 17, 16],
            1: [12], 2: [8], 3: [6], 4: [2], 5: [13]
        },
        '15-5s_h': {
            0: [0, 12, 9, 19, 6, 4, 10, 5, 18, 14, 15, 16, 3, 8, 7, 11],
            1: [13], 2: [2], 3: [20], 4: [17], 5: [1]
        },
        '15-5s_i': {
            0: [0, 13, 10, 15, 8, 7, 19, 4, 3, 16, 12, 14, 11, 5, 20, 6],
            1: [2], 2: [18], 3: [9], 4: [17], 5: [1]
        },
        '15-5s_j': {
            0: [0, 1, 14, 9, 5, 2, 15, 8, 20, 6, 16, 18, 7, 11, 10, 19],
            1: [3], 2: [4], 3: [17], 4: [12], 5: [13]
        },
        '15-5s_k': {
            0: [0, 16, 13, 1, 11, 12, 18, 6, 14, 5, 3, 7, 9, 20, 19, 15],
            1: [4], 2: [2], 3: [10], 4: [8], 5: [17]
        },
        '15-5s_l': {
            0: [0, 10, 7, 6, 19, 16, 8, 17, 1, 14, 4, 9, 3, 15, 11, 12],
            1: [2], 2: [18], 3: [20], 4: [13], 5: [5]
        },
        '15-5s_m': {
            0: [0, 18, 4, 14, 17, 12, 10, 7, 3, 9, 1, 8, 15, 6, 13, 2],
            1: [5], 2: [11], 3: [20], 4: [16], 5: [19]
        },
        '15-5s_n': {
            0: [0, 5, 4, 13, 18, 14, 10, 19, 15, 7, 9, 3, 2, 8, 16, 20],
            1: [1], 2: [12], 3: [11], 4: [6], 5: [17]
        },
        '15-5s_o': {
            0: [0, 9, 12, 13, 18, 7, 1, 15, 17, 10, 8, 4, 5, 20, 16, 6],
            1: [14], 2: [19], 3: [11], 4: [2], 5: [3]
        },
        '15-5s_p': {
            0: [0, 9, 12, 13, 18, 2, 11, 15, 17, 10, 8, 4, 5, 20, 16, 6],
            1: [14], 2: [19], 3: [1], 4: [7], 5: [3]
        },
        '15-5s_q': {
            0: [0, 3, 14, 13, 18, 2, 11, 15, 17, 10, 8, 4, 5, 20, 16, 6],
            1: [12], 2: [19], 3: [1], 4: [7], 5: [9]
        },
        '15-5s_r': {
            0: [0, 3, 14, 13, 1, 2, 11, 15, 17, 7, 8, 4, 5, 9, 16, 19],
            1: [12], 2: [6], 3: [18], 4: [10], 5: [20]
        },
        '15-5s_s': {
            0: [0, 3, 14, 6, 1, 2, 11, 12, 17, 7, 20, 4, 5, 9, 16, 19],
            1: [15], 2: [13], 3: [18], 4: [10], 5: [8]
        }, 
        '15-5s_t': {
            0: [0, 3, 15, 13, 1, 2, 11, 18, 17, 7, 20, 8, 5, 9, 16, 19],
            1: [14], 2: [6], 3: [12], 4: [10], 5: [4]
        },
        '15-5s_u': {
            0: [0, 3, 15, 13, 14, 6, 11, 18, 17, 7, 20, 8, 4, 9, 16, 10],
            1: [1], 2: [2], 3: [12], 4: [19], 5: [5]
        },
        '15-5s_v': {
            0: [0, 1, 2, 12, 14, 6, 19, 18, 17, 5, 20, 8, 4, 9, 16, 10],
            1: [3], 2: [15], 3: [13], 4: [11], 5: [7]
        },
        '15-5s_w': {
            0: [0, 1, 2, 12, 14, 13, 19, 18, 7, 11, 20, 8, 4, 9, 16, 10],
            1: [3], 2: [15], 3: [6], 4: [5], 5: [17]
        },
        '10-1': {
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            1: [11], 2: [12], 3: [13], 4: [14], 5: [15], 6: [16], 7: [17], 8: [18], 9: [19], 10: [20]
        },
    }
    def __init__(self, mode, dataset_cfg):
        super(VOCDataset, self).__init__(mode, dataset_cfg)
    '''builddatagenerator'''
    def builddatagenerator(self, mode, dataset_cfg):
        data_generator = _VOCDataset(mode, dataset_cfg)
        return data_generator