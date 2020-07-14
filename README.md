[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Skellet0r/customer-churn/master)

# Telecommunications Customer Churn Classification

## Components

- [Charter](docs/project/charter.md): the project charter was the first step when
  starting this project, and is a sort of outline of this project. It clarifies
  who our stakeholders are, what we aim to do, and how we intend to complete this
  project. If this is your first time looking at this project, the project charter
  is the best place to start.
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

## Quick Start

If you want to have a quick interactive environment I recommend you launch the binder instance of this project
by clicking the 'launch binder' tag at the top of this readme.

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

