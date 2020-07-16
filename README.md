[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Skellet0r/customer-churn/master)

# Telecommunications Customer Churn Classification

This is a classification project, aiming to predict which customers will soon end their service plan with our client.
This has a large business value to our client as their customer churn rate is above 14%, and lowering that rate means
more profit.

The presentation delivered to stakeholders for this project can be found [here](https://Skellet0r.github.io/customer-churn).

## Components

- [Charter](docs/project/charter.md): the project charter was the first step when
  starting this project, and is a sort of outline of this project. It clarifies
  who our stakeholders are, what we aim to do, and how we intend to complete this
  project. If this is your first time looking at this project, the project charter
  is the best place to start.
- [Exit Report](docs/project/exit-report.md): a quick outline of the end results of this
  project. It isn't an exhaustive report, however along with the project charter it gives
  a quick overview of what this project is and what was accomplished.
- [Data](data/): this is where data used in this project is stored. It is separated by
  which phase the data is in, either raw, interim, or processed.
- [Notebooks](notebooks/): this is where all the jupyter notebooks for this project are
  stored. Instead of having one behemoth of a jupyter notebook, there are multiple
  distinct notebooks each focusing on a different phase of the project. A majority
  of the notebooks focus on modeling and using different classifiers. Each notebook
  is numbered in the order they were completed, this keeps everything in a linear
  order.
- [Src](src/): this is were custom python functions/variables are stored that are
  used throughout the project. It is installed into the conda environment when
  you first create the environment, and any changes automagically appear.
- [Environment](environment.yml): this is a conda environment.yml file, which allows
  one to consistently reproduce the same clean working environment.
- [Presenation](https://Skellet0r.github.io/customer-churn): the presentation delivered to stakeholders.

## Quick Start

For a quick interactive environment launch this project's binder instance by click the
`lauch binder` tag.

If you want your own local instance of this project follow the steps below.

1. Clone this repository

```shell
$ git clone https://github.com/Skellet0r/customer-churn.git
```

2. Initialize the environment

```shell
$ cd ./customer-churn
$ conda env create -f environment.yml
```

3. Activate the environment

```shell
$ conda activate customer-churn
```

4. Enjoy 😃

## Final Model Results

Our final model was tested on our hold out set after preprocessing. Our results are shown below.

|               | Precision | Recall   | Accuracy | F1       |
| ------------- | --------- | -------- | -------- | -------- |
| Final Testing | 0.877193  | 0.826446 | 0.958034 | 0.851064 |

Looking at the ROC/AUC Curve of the model we can see it has a great degree of separability between the two classes.

![ROC/AUC Curve Testing](docs/visuals/04-final-model-roc-auc-curve.png)

## Recommendations

Looking at the importance of features in our model we see that the amount of minutes and by extension the total charge a customer incurs is the
most important feature in determining whether a customer will soon stop their service plan.

![Feature Importance Top 5](docs/visuals/01-top-5-features.svg)
