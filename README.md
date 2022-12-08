# ozone_investigation
Programming Project for investigating ozone layers in the scope of the lecture "Special Topics Data Handling and Programming in Climate Science"

The project can be installed in your environment (preferably virtual environment) using `pip`.

It provides the following shell script: `ozone_investigation`.
For usage information, type `ozone_investigation --help`.

## Installation

Use the following command to install:

```bash
python -m pip install <project_path>
```

For an editable ("developer mode") installation, use the following
instead:

```bash
python -m pip install -e <project_path>
```

With this, the installation is actually a link to the original source code,
i.e. each change in the source code is immediately available.


## Prerequisites

You need a working Python environment, and `pip` installed.

E.g., with `conda`:

```bash
conda create --name mynewenv python
conda activate mynewenv
python -m pip install -e .
```
Moreover, it is necessary to install the following libraries beforehand, if working with an Ubuntu system:

```bash
sudo apt-get install libproj-dev proj-data proj-bin
sudo apt-get install libgeos-dev
conda install cython
conda install cartopy 
```

## Notes
