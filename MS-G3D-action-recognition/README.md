# MS-G3D fine-grained Action Recognition baseline for Assembly101

PyTorch implementation of MS-G3D ("Disentangling and Unifying Graph Convolutions for Skeleton-Based Action Recognition", CVPR 2020 Oral) used for fine-grained Action Recognition task in the paper:

F. Sener et al. "**Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities**", CVPR 2022 [[paper](https://arxiv.org/pdf/2203.14712.pdf)]

This repository has been adapted from the original [MS-G3D repository](https://github.com/kenziyuliu/MS-G3D) to train and evaluate on the Assembly101 dataset.

## Contents
* [Overview](#overview)
* [Data](#data)
* [Training](#training)
* [Evaluate](#evaluate)
* [Acknowledgements](#acknowledgements)

## Overview

This repository provides codes to train, validate and generate test set predictions for the task of fine-grained action recognition of the Assembly101 dataset.

## Data

Run [`Preprocess/1_generate_pose_data.py`](Preprocess/1_generate_pose_data.py) followed by [`Preprocess/2_get_final_dataset.py`](Preprocess/2_get_final_dataset.py) to generate MS-G3D style data and annotations from the .json hand poses and .csv annotations.

```bash
python Preprocess/1_generate_pose_data.py
python Preprocess/2_get_final_dataset.py
```

Hand pose data can be found in this [repository](https://drive.google.com/drive/folders/1tQbqbXdGfU40kBKfXN4TpKru0s5O4LIa). 
Please refer to our [annotations repository](https://github.com/assembly-101/assembly101-annotations) for CSV files and further information regarding Assembly101 annotations.

Note that, the 3D hand poses are extracted at 60fps in contrast to the frames in the server and the annotations which are at 30fps.

In the [`HAND_GCN`](HAND_GCN) folder's subfolder [`share_contex25_thresh0`](data/share_contex25_thresh0), we already provide MS-G3D styled fine-grained action annotations for training and validation set taking 25 frames of context from both ends with no minimum confidence threshold for pose data. The files are:

| File name | Description |
|-----------|-------------|
| train_data_joint_200.npy | A concatenated numpy array containing 200 frames of hand poses per segment for all training segments |
| train_label.pkl | A list of filenames (segment identifiers) and their action labels stored in the same order as train_data_joint_200.npy|
| validation_data_joint_200.npy | A concatenated numpy array containing 200 frames of hand poses per segment for all validation segments |
| validation_label.pkl | A list of filenames (segment identifiers) and their action labels stored in the same order as validation_data_joint_200.npy|


## Training

To train our model, run [`MS_3GD/train_model.py`](MS_3GD/train_model.py). Model parameters are set in [`MS_3GD/train_config.yaml`](MS_3GD/train_config.yaml)

```bash
python MS_3GD/train_model.py
```

## Evaluate

To evaluate our model, run [`MS_3GD/test_model.py`](MS_3GD/train_model.py). Model parameters are set in [`MS_3GD/test_config.yaml`](MS_3GD/train_config.yaml), which is currently configured to use the validation set.

```bash
python MS_3GD/test_model.py
```


## Acknowledgements

Grateful to the collaborators/maintainers of the [MS-G3D repository](https://github.com/kenziyuliu/MS-G3D).