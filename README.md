montecarlo
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/montecarlo/workflows/CI/badge.svg)](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/montecarlo/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/montecarlo/branch/main/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/montecarlo/branch/main)


Monte Carlo Simulation Package

### Copyright

Copyright (c) 2026, Olivia Watt

# Installation
You will need an environment with the following packages:
* Python 3.11
* NumPy
* Matplotlib
Once you have these packages installed, you can install montecarlo in the same environment using
```sh
pip install -e .
```
from the top-level montecarlo/ directory.

# Usage
To use montecarlo in a project:
```python
import montecarlo

# Define a new configuration instance for a 6-site lattice
conf = montecarlo.BitString(6)


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.11.
