## Kaggle SIIM-ISIC Melanoma Classification: 3rd place solution overview

Competition Leaderboard: https://www.kaggle.com/c/siim-isic-melanoma-classification/leaderboard

---

### Software

Model training and predictions were performed in Kaggle TPU Kernels.

* Python 3.7.6
* Kaggle's TPU v3-8 (8 cores)
* Python packages are detailed separately in `requirements.txt`

---

### Image models:

#### Training

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

#### Predicting

---

### Metadata: Training & Predicting
https://www.kaggle.com/titericz/simple-baseline

---

### Ensembling


