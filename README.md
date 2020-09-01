# Kaggle SIIM-ISIC Melanoma Classification

## 3rd place solution overview

Competition Leaderboard: https://www.kaggle.com/c/siim-isic-melanoma-classification/leaderboard

### Software

* Python 3.7.6
* Kaggle's TPU v3-8 (8 cores)
* Python packages are detailed separately in `requirements.txt`

### Setup Python environment

```
pip install -r requirements.txt
```

### Download data

Assumes the [Kaggle API](https://github.com/Kaggle/kaggle-api) is installed.

```
mkdir ./data
cd ./data
```
#### Competition data:
```
kaggle competitions download -c siim-isic-melanoma-classification
unzip siim-isic-melanoma-classification.zip
rm siim-isic-melanoma-classification.zip
```
#### Images of hairs for hair augmentation:
```
kaggle datasets download -d nroman/melanoma-hairs
unzip -q melanoma-hairs.zip -d melanoma-hairs
rm melanoma-hairs.zip
```
#### TFRecords:
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

