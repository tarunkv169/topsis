# TOPSIS Analysis Package

A Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on numerical datasets. This package provides both a command-line interface and a importable module for performing TOPSIS analysis on datasets containing numerical data (int32, int64, float32, float64).

## Overview

TOPSIS is a multi-criteria decision analysis method that helps identify the best alternative from a set of options based on multiple criteria. The package normalizes the input data, applies weights to different criteria, and considers whether each criterion should be maximized or minimized.

## Installation

```bash
pip install topsis-102217133
```

## Usage

### As a Module

```python
from topsis_analysis import run

# Perform TOPSIS analysis
result_df = run(
    input_df,           # pandas DataFrame with numerical values
    weights,            # List of weights for each criterion
    impacts,            # List of impacts ('+' or '-') for each criterion
)
```

### Command Line Interface

```bash
python -m topsis_analysis <source_csv> <weights> <impacts> <output_csv>
```

### Parameters

#### For Both Module and CLI:

1. Input Data:
   - Must contain only numerical values (int32, int64, float32, float64)
   - First column will be used as index
   - No missing values allowed

2. Weights:
   - Must sum to 1
   - Number of weights must match number of columns (excluding index)
   - Module: List of float values
   - CLI: Comma-separated values (e.g., "0.25,0.25,0.25,0.25")

3. Impacts:
   - Use '+' for criteria to be maximized
   - Use '-' for criteria to be minimized
   - Number of impacts must match number of columns (excluding index)
   - Module: List of strings
   - CLI: Comma-separated signs (e.g., "-,+,+,+")

#### CLI Only:

4. `output_csv`: Path where the result CSV will be stored

### Example Usage

#### As a Module

```python
import pandas as pd
from topsis_analysis import run

# Read input data
df = pd.read_csv('data.csv')

# Define weights and impacts
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['-', '+', '+', '+']

# Run TOPSIS analysis
result = run(df, weights, impacts)

# Save results if needed
result.to_csv('output.csv', index=False)
```

#### Command Line

```bash
python -m topsis-102217133 data.csv 0.25,0.25,0.25,0.25,0.25 -,+,+,+,+ output.csv
```

### Input CSV Format

```csv
P1,P2,P3,P4,P5
0.62,0.38,5.7,47,13.43
0.8,0.64,5.4,38.6,11.36
0.83,0.69,3.3,57.9,15.68
0.84,0.71,5.5,52.3,14.84
0.72,0.52,4.6,44.8,12.66
0.61,0.37,7,41.2,12.3
0.61,0.37,3.9,46.7,12.9
0.93,0.86,6.5,35.4,10.92

```

- Weights not summing to 1
### Output Format

```csv
P1,P2,P3,P4,P5,euclidean_distance_worst,euclidean_distance_best,performance_score,rank
0.29077553802544853,0.22636699320773462,0.37551232309446086,0.361269319952853,0.36248022622053017,0.18911380785500428,0.350388690096909,0.35053370201792894,7
0.375194242613482,0.3812496727709215,0.35574851661580503,0.296702037237875,0.30661022858266734,0.29757811013334073,0.18096741720614892,0.6218386613866165,2

```

## Error Handling

The package provides comprehensive error handling for:
- Invalid number of weights or impacts
- Invalid data types
- Missing values in the dataset
- Invalid file paths (CLI only)
- Non-numeric data in columns
- Invalid impact symbols

## Dependencies

- Python 3.7+
- pandas
- numpy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.