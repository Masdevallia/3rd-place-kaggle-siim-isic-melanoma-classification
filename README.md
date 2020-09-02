## Kaggle SIIM-ISIC Melanoma Classification: 3rd place solution overview

Competition Leaderboard: https://www.kaggle.com/c/siim-isic-melanoma-classification/leaderboard

### Software

Model training and predictions were performed in Kaggle TPU Kernels.

* Python 3.7.6
* Kaggle's TPU v3-8 (8 cores)
* Python packages are detailed separately in `requirements.txt`

### Training

#### Image models:

| Model       | Data        | Image size    | Epochs            | Hair augmentation |
| :----:      |    :----:   |      :----:   |      :----:       |      :----:       |
| 1           | 2020        | 256x256       | 13                |                   |
| 2           | 2020        | 384x384       | 15                |                   |
| 3           | 2020        | 512x512       | 15                |                   |
| 4           | 2020        | 768x768       | 15                |                   |
| 5           | 2019-2020   | 256x256       | 25                | X                 |
| 6           | 2019-2020   | 384x384       | 25                | X                 |
| 7           | 2019-2020   | 512x512       | 12                | X                 |
| 8           | 2019-2020   | 768x768       | 10                |                   |

Trained weights can be found [here](https://www.kaggle.com/masdevallia/melanoma-classification-3rd-place-models).

#### Metadata

https://www.kaggle.com/titericz/simple-baseline

### Predicting

### Ensembling

### Appendix

#### How to download competition data locally

Assumes the [Kaggle API](https://github.com/Kaggle/kaggle-api) is properly installed.

```
mkdir ./data
cd ./data
```
##### Competition data
```
kaggle competitions download -c siim-isic-melanoma-classification
unzip siim-isic-melanoma-classification.zip
rm siim-isic-melanoma-classification.zip
```
##### Images of hairs for hair augmentation
```
kaggle datasets download -d nroman/melanoma-hairs
unzip -q melanoma-hairs.zip -d melanoma-hairs
rm melanoma-hairs.zip
```
##### TFRecords
```
for input_size in 256 384 512 768
do
  # 2020 TFRecords:
  kaggle datasets download -d cdeotte/melanoma-${input_size}x${input_size}
  unzip -q melanoma-${input_size}x${input_size}.zip -d melanoma-${input_size}x${input_size}
  rm melanoma-${input_size}x${input_size}.zip
  # 2017-2018-2019 TFRecords:
  kaggle datasets download -d cdeotte/isic2019-${input_size}x${input_size}
  unzip -q isic2019-${input_size}x${input_size}.zip -d isic2019-${input_size}x${input_size}
  rm isic2019-${input_size}x${input_size}.zip
done
```

