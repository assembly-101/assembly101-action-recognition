# TSM fine-grained Action Recognition baseline for Assembly101

PyTorch implementation of Temporal Shift Module (TSM) used for fine-grained Action Recognition task in the paper:

F. Sener et al. "**Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities**", CVPR 2022 [[paper](https://arxiv.org/pdf/2203.14712.pdf)]

This repository has been adapted from the original [TSM repository](https://github.com/mit-han-lab/temporal-shift-module) to train and evaluate on the Assembly101 dataset.

## Contents
* [Overview](#overview)
* [Data](#data)
* [Training](#training)
    * [Pretrained Models](#pretrained-models)
* [Evaluate](#evaluate)
* [Acknowledgements](#acknowledgements)

## Overview

This repository provides codes to train, validate and generate test set predictions for the task of fine-grained action recognition of the Assembly101 dataset.

## Data

Run [`gen_fine_labels.py`](/gen_fine_labels.py) like below to generate TSM-style .txt annotations from the .csv files provided by us. 

```bash
python gen_fine_labels.py arg1 arg2
```
| arguments | Remarks |
|-----------|---------|
| arg1 | `modality` argument <br> options: <br> `rgb`: generate action segments for only the 8 fixed (RGB) views <br> `mono`: generate action segments for only the 4 egocentic (mono) views <br> `combined`: generate action segments for all the 12 views |
| arg2 | `split` argument <br> options: `train` / `validation` / `test` |

Please refer to our [annotations repository](https://github.com/assembly-101/assembly101-annotations) for further information regarding Assembly101 annotations.

In the [`data`](/data) folder, we already provide TSM-style `.txt` fine-grained action annotations for all 12 views (combined). The files are

| File name | Description |
|-----------|-------------|
| category.txt | a list of 1380 fine-grained actions |
| train_combined_{`1/2/3`}.txt | training annotations of the format: <br> {`sequence_name`}/{`view_name`} <br> `start_frame` <br> `num_frames` <br> `label` <br> <br> **combined** means both the fixed (RGB) and egocentric (mono) views are used for training (check view mappings [here](https://github.com/assembly-101/assembly101-download-scripts#which-camera_ids-correspond-to-which-views-)) <br> the .txt is divided into 3 files due to file size limit |
| validation_combined.txt | validation annotations of the same format as the training |
| test_combined.txt | test annotations of the same format as the training <br> the labels are withheld as `-1` for challenge purposes |

## Training

To train our model, run `main.py`. Following is an example to start with a TSM pretrained on EPIC-KITCHENS-100 and fine-tune Assembly101.

```bash
python main.py Assembly101 combined --arch resnet50 --num_segments 8 --gd 20 --lr 0.001 --lr_steps 20 40 --epochs 50 --batch-size 64 -j 16 --dropout 0.5 --consensus_type=avg --eval-freq=1 --shift --shift_div=8 --shift_place=blockres --npb --tune_from=pretrained_models/tsm_rgb_epic.ckpt
```

### Pretrained Models

Check the [pretrained_models](/pretrained_models/) folder to download the pretrained TSM models.

## Evaluate

To evaluate our model, run `test_models.py`. The following example will evaluate the model on the validation set:

```bash
python test_models.py Assembly101 --weights="path_to_weight" --test_segments 8 --batch_size 64 -j 16 --test_crops 1
```

To generate action predictions for the test set, run `test_models.py` with test_combined.txt as the text_file like the following:

```bash
python test_models.py Assembly101 --weights="path_to_weight" --test_segments 8 --batch_size 64 -j 16 --test_crops 1 --text_file data/test_combined.txt
```
The code outputs the evaluation set (validation/test) predictions in the form of two numpy files:
| File name | Description |
|-----------|-------------|
| preds.npy | fine-grained action predictions (numeric labels) per segments following the order in the .txt file. The labels follow the action index convention as present in the `data/category.txt` |
| scores.npy | fine-grained action prediction scores per segments following the order in the .txt file. The scores per segment are 1380-dim vectors corresponding to the 1380 fine-grained action classes. |

**As mentioned previously, we hold the ground truth test labels for a challenge we are organizing. Therefore, to measure the test set accuracy, please submit your test predictions to our challenge website (coming soon).**

For further infomation regarding training/validation/testing, kindly check the original [TSM repository](https://github.com/mit-han-lab/temporal-shift-module#testing).

## Acknowledgements

Grateful to the collaborators/maintainers of the [TSM repository](https://github.com/mit-han-lab/temporal-shift-module).
