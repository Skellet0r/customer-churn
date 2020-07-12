"""
This setup.py allows for the src directory to be pip installed.
This means scripts/modules/functions in the src directory will be
available in the environment such as in jupyter notebooks.

Additional fields are left blank but can be filled in optionally.

To install:
pip install -e .
--or--
pip install -r requirements.txt

To make it even easier we can add the package to the environment.yml
having a requirements.txt is only a convenience.

https://github.com/conda/conda/blob/54e4a91d0da4d659a67e3097040764d3a2f6aa16/tests/conda_env/support/advanced-pip/environment.yml
"""

import setuptools

setuptools.setup(
    name="src",
    version="v1.0.0",
    author="Edward Amor",
    author_email="edward.amor3@gmail.com",
    description="Custom functions for customer churn data science project",
    url="https://github.com/Skellet0r/customer-churn",
    packages=setuptools.find_packages(),
    install_requires=["pandas", "numpy", "scikit-learn", "xgboost", "imblearn",],
)
