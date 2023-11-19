<div align="center">
  <img src="./docs/logo.png" width="600"/>
</div>
<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](https://cssegmentation.readthedocs.io/en/latest/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cssegmentation)](https://pypi.org/project/cssegmentation/)
[![PyPI](https://img.shields.io/pypi/v/cssegmentation)](https://pypi.org/project/cssegmentation)
[![license](https://img.shields.io/github/license/SegmentationBLWX/cssegmentation.svg)](https://github.com/SegmentationBLWX/cssegmentation/blob/master/LICENSE)
[![PyPI - Downloads](https://pepy.tech/badge/cssegmentation)](https://pypi.org/project/cssegmentation/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/cssegmentation?style=flat-square)](https://pypi.org/project/cssegmentation/)
[![issue resolution](https://isitmaintained.com/badge/resolution/SegmentationBLWX/cssegmentation.svg)](https://github.com/SegmentationBLWX/cssegmentation/issues)
[![open issues](https://isitmaintained.com/badge/open/SegmentationBLWX/cssegmentation.svg)](https://github.com/SegmentationBLWX/cssegmentation/issues)

Documents: https://cssegmentation.readthedocs.io/en/latest/


## Introduction

CSSegmentation: An Open Source Continual Semantic Segmentation Toolbox Based on PyTorch.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.


## Major Features

- **High Performance**

  The performance of re-implemented CSS algorithms is better than or comparable to the original paper.
 
- **Modular Design and Unified Benchmark**
  
  Various CSS methods are unified into several specific modules.
  Benefiting from this design, CSSegmentation can integrate a great deal of popular and contemporary continual semantic segmentation frameworks and then, train and test them on unified benchmarks.
  
- **Fewer Dependencies**

  CSSegmentation tries its best to avoid introducing more dependencies when reproducing novel continual semantic segmentation approaches.
  

## Benchmark and Model Zoo

#### Supported Encoder

| Encoder                | Model Zoo                                                   | Paper Link                                                    | Code Snippet                                             |
| :-:                    | :-:                                                         | :-:                                                           | :-:                                                      |
| ResNet                 | [click](./docs/modelzoo/mib)                                | [CVPR 2016](https://arxiv.org/pdf/1512.03385.pdf)             | [click](./csseg/modules/models/encoders/resnet.py)       |

#### Supported Decoder

| Decoder                | Model Zoo                                                   | Paper Link                                                    | Code Snippet                                             |
| :-:                    | :-:                                                         | :-:                                                           | :-:                                                      |
| Deeplabv3              | [click](./docs/modelzoo/mib)                                | [ArXiv 2017](https://arxiv.org/pdf/1706.05587.pdf)            | [click](./csseg/modules/models/decoders/aspphead.py)     |

#### Supported Runner

| Runner                 | Model Zoo                                                   | Paper Link                                                                                                                                                                            | Code Snippet                                             |
| :-:                    | :-:                                                         | :-:                                                                                                                                                                                   | :-:                                                      |
| EWF                    | [click (under developing)](./docs/modelzoo/ewf)                                | [CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/papers/Xiao_Endpoints_Weight_Fusion_for_Class_Incremental_Semantic_Segmentation_CVPR_2023_paper.pdf)                       | [click](./csseg/modules/runners/ewf.py)                  |
| UCD                    | [click (under developing)](./docs/modelzoo/ucd)                                | [TPAMI 2022](https://arxiv.org/pdf/2203.14098.pdf)                                                                                                                                    | [click](./csseg/modules/runners/ucd.py)                  |
| RCIL                   | [click (under developing)](./docs/modelzoo/rcil)                               | [CVPR 2022](https://arxiv.org/pdf/2203.05402.pdf)                                                                                                                                     | [click](./csseg/modules/runners/rcil.py)                 |
| REMINDER               | [click (under developing)](./docs/modelzoo/reminder)                           | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/papers/Phan_Class_Similarity_Weighted_Knowledge_Distillation_for_Continual_Semantic_Segmentation_CVPR_2022_paper.pdf)      | [click](./csseg/modules/runners/reminder.py)             |
| CAF                    | [click (under developing)](./docs/modelzoo/caf)                                | [TMM 2022](https://arxiv.org/pdf/2202.00432.pdf)                                                                                                                                      | [click](./csseg/modules/runners/caf.py)                  |
| SDR                    | [click (under developing)](./docs/modelzoo/sdr)                                | [CVPR 2021](https://arxiv.org/pdf/2103.06342.pdf)                                                                                                                                     | [click](./csseg/modules/runners/sdr.py)                  |
| PLOP                   | [click](./docs/modelzoo/plop)                               | [CVPR 2021](https://arxiv.org/pdf/2011.11390.pdf)                                                                                                                                     | [click](./csseg/modules/runners/plop.py)                 |
| MIB                    | [click](./docs/modelzoo/mib)                                | [CVPR 2020](https://arxiv.org/pdf/2002.00718.pdf)                                                                                                                                     | [click](./csseg/modules/runners/mib.py)                  |
| ILT                    | [click](./docs/modelzoo/ilt)                                | [ICCVW 2019](https://arxiv.org/pdf/1907.13372.pdf)                                                                                                                                    | [click](./csseg/modules/runners/ilt.py)                  |

#### Supported Datasets

| Dataset                | Project Link                                                                               | Paper Link                                                                                | Code Snippet                                             |
| :-:                    | :-:                                                                                        | :-:                                                                                       | :-:                                                      |
| ADE20k                 | [Click](https://groups.csail.mit.edu/vision/datasets/ADE20K/)                              | [CVPR 2017](https://arxiv.org/pdf/1608.05442.pdf)                                         | [Click](./csseg/modules/datasets/ade20k.py)              |
| PASCAL VOC             | [Click](http://host.robots.ox.ac.uk/pascal/VOC/)                                           | [IJCV 2010](http://host.robots.ox.ac.uk/pascal/VOC/pubs/everingham10.pdf)                 | [Click](./csseg/modules/datasets/voc.py)                 |


## Citation

If you use this framework in your research, please cite this project:

```
@misc{csseg2023,
    author = {Zhenchao Jin},
    title = {CSSegmentation: An Open Source Continual Semantic Segmentation Toolbox Based on PyTorch},
    year = {2023},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/SegmentationBLWX/cssegmentation}},
}
```