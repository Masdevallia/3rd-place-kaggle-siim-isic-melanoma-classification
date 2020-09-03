## Kaggle SIIM-ISIC Melanoma Classification: 3rd place solution overview

Competition Leaderboard: https://www.kaggle.com/c/siim-isic-melanoma-classification/leaderboard

Solution overview: https://www.kaggle.com/c/siim-isic-melanoma-classification/discussion/175633

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

For example, for model 1, the content of the input cell should be:
```python
tfrec_shape = 256
comp_data = "2020"
```

For model 6, however, it should be:
```python
tfrec_shape = 384
comp_data = "2019-2020"
```

Training time for a single model ranges from ~ 0.5 to ~ 3 hours (all models can be fitted within 3 hours Kaggle's TPU limit for a single session).

Our trained weights can be found [here](https://www.kaggle.com/masdevallia/melanoma-classification-3rd-place-models).

#### Predicting

The source code for making predictions is published in this [Kaggle notebook](https://www.kaggle.com/masdevallia).

Again, to reproduce our results, the Kaggle notebook must be forked and executed 8 times, one for each model, changing only the content of the first cell (input) each time.

Our image-models submission files can be found in `"./submissions/image_data"`.

---

### Metadata

#### Training & Predicting

For metadata, we used a simple baseline model proposed by [@titericz](https://www.kaggle.com/titericz), which can be found [here](https://www.kaggle.com/titericz/simple-baseline).

Our metadata-model submission file can be found in `"./submissions/metadata"`.

---

### Ensembling

The script `ensembling.py` ensembles the image-models submission files located in `"./submissions/image_data"` whit a single metadata-model submission file located in `"./submissions/metadata"`. The script allows you to choose whether to include external data (e.g. from other public notebooks) or not. External image-models submissions must be located in `"./submissions/external_image_data"`. The resulting ensemble file is saved in the destination path: `"./ensemble"`.

#### Usage:

```
python ensembling.py [-h] [--include_external EXTERNAL] [--metadata_weight WEIGHT] [--ensemble_filename FILENAME]
```

|         Argument               |         Function                            |     Default   |
|           :----:               |         :----:                              |      :----:   |
|        -h, --help              |      Shows help message and exits           |               |
| --include_external EXTERNAL    | Whether to include external data (1) or not (0) |     0     |
|     --metadata_weight WEIGHT   |      Weight assigned to metadata (0-1)      |    0.2        |
|   --ensemble_filename FILENAME |   The desired name for the ensemble file    |    'ensemble' |

#### Our solutions:

Our winning solution, which scored 0.9484 private LB, 0.9620 public LB, was obtained by the following parameterization:

```
python ensembling.py --include_external 1 --metadata_weight 0.3 --ensemble_filename 'ensemble_external'
```

In this solution, we decided to ensemble two public notebooks to our image-models, in order to add some diversity ([this one](https://www.kaggle.com/rajnishe/rc-fork-siim-isic-melanoma-384x384) from [@rajnishe](https://www.kaggle.com/rajnishe) and [this one](https://www.kaggle.com/ajaykumar7778/efficientnet-cv) from [@ajaykumar7778](https://www.kaggle.com/ajaykumar7778)). The corresponding ensemble file can be found in `"./ensemble/ensemble_external.csv"`.

However, a higher score can be obtained without using external data, with the following parameterization:

```
python ensembling.py --include_external 0 --metadata_weight 0.2 --ensemble_filename 'ensemble'
```

The last ensemble scored 0.9489 private LB, 0.9592 public LB, but was not selected as a final submission for judging. It can be found in `"./ensemble/ensemble.csv"`.
