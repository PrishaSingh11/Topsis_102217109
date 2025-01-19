# TOPSIS Python Package and CLI

## Overview

This repository contains two components for implementing the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method:
1. A Python CLI script for ranking alternatives using TOPSIS.
2. A Python package published on PyPI.

The TOPSIS method is a multi-criteria decision analysis (MCDA) technique used to evaluate and rank alternatives based on multiple criteria.

---

## Python Package: 102217109_topsis

### Features:
- Easy-to-use function to perform the TOPSIS method on decision matrices.
- Accepts customizable weights for each criterion.
- Supports both beneficial and non-beneficial criteria (impacts).
- Returns preference scores and ranks for the alternatives.

#### Parameters:
- **data** (list of lists): Decision matrix (alternatives x criteria).
- **weights** (list): List of weights for each criterion.
- **impacts** (list): '+' for beneficial, '-' for non-beneficial criteria.

#### Returns:
- **list**: Preference scores for each alternative.
- **list**: Ranks of each alternative.

### Installation
You can install the package from PyPI:
```bash
pip install 102217109_topsis
```
### Usage
After installing the package, you can use the TOPSIS functionality in Python:
```bash
from topsis import topsis
```

## Python CLI Script
This repository also includes a Python Command Line interface implementaion of the TOPSIS method.It allows users to process a decision matrix directly from a CSV file and generate ranked results.

### Files Included
- **102217109_topsis-cli.py**: The Python CLI script for TOPSIS.
-  **102217109-Data.csv**: Example input data file.
- **102217109_output.csv**: Example output file.

### How to use the CLI
1. Prepare your input data as a CSV file (e.g., 102217109-Data.csv).
2. Run the CLI script with the following command:
```bash
python 102217109_topsis-cli.py 102217109-Data.csv 0.3,0.4,0.3 +,-,+ 102217109_output.csv
```
- First Argument: Input CSV file.
- Second Argument: Weights for the criteria (comma-separated).
- Third Argument: Impacts for the criteria ('+' or '-' comma-separated).
- Fourth Argument: Output CSV file name.
3. The output file will contain the preference scores and ranks for each alternative.



