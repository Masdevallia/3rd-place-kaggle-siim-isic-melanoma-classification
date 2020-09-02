## Kaggle SIIM-ISIC Melanoma Classification: 3rd place solution overview

Competition Leaderboard: https://www.kaggle.com/c/siim-isic-melanoma-classification/leaderboard

---

### Software

Model training and predictions were performed in Kaggle TPU Kernels.

* Python 3.7.6
* Kaggle's TPU v3-8 (8 cores)
* Python packages are detailed separately in `requirements.txt`

---

### Image models

#### Training

The source code for model training is published in this [Kaggle notebook](https://www.kaggle.com/masdevallia).

We trained 8 image models, as shown below:

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

To reproduce our results, the Kaggle notebook must be forked and executed 8 times, one for each model, changing only the content of the first cell (input) each time.

For example, for the model 1, the content of the input cell should be:
```python
tfrec_shape = 256
comp_data = "2020"
```

For model 6, however, it should be:
```python
tfrec_shape = 384
comp_data = "2019-2020"
```

Our trained weights can be found [here](https://www.kaggle.com/masdevallia/melanoma-classification-3rd-place-models).

#### Predicting

The source code for making predictions is published in this [Kaggle notebook](https://www.kaggle.com/masdevallia).

Again, to reproduce our results, the Kaggle notebook must be forked and executed 8 times, one for each model, changing only the content of the first cell (input) each time.

Our image-models submission files can be found in `"./submissions/image_data/"`.

---

### Metadata

#### Training & Predicting

For metadata, we used a simple baseline model proposed by [@titericz](https://www.kaggle.com/titericz), which can be found [here](https://www.kaggle.com/titericz/simple-baseline).

Our metadata-model submission file can be found in `"./submissions/metadata/"`.

---

### Ensembling

The script `ensembling.py` ensembles the image-models submission files located in `"./submissions/image_data/"` whit the metadata-model submission file located in `"./submissions/metadata/"`.

Usage:

```
python ensembling.py [-h] [--image_data_path PATH] [--metadata_path PATH] [--metadata_weight WEIGHT] [--ensemble_path PATH] [--ensemble_filename FILENAME]
```

|         Argument           |         Function                           |     Default   |
|           :----:           |         :----:                             |      :----:   |
|        -h, --help          |      Shows help message and exits          |               |
| --image_data_path PATH    |      Path to image-models submission files | './submissions/image_data' |
| --metadata_path PATH     | Path to the metadata-model submission file | './submissions/metadata' |
| --metadata_weight WEIGHT   |        Weight assigned to metadata         |    0.2        |
| --ensemble_path PATH     | The desired destination path in which to save the ensemble file | './ensemble' |
| --ensemble_filename FILENAME |   The desired name for the ensemble file   |    'ensemble' |