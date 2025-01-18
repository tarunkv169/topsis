from algo import run
import sys
import pandas as pd

def valid_operators(value):
    operators = value.split(',')  # Split by comma
    valid_ops = ['+', '-']
    for op in operators:
        if op not in valid_ops:
            raise argparse.ArgumentTypeError(f"Invalid operator: '{op}'. Allowed operators are {valid_ops}.")
    return operators

def valid_numbers(value):
    try:
        numbers = [float(num) for num in value.split(',')]
        return numbers
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid numbers. Provide a comma-separated list of numbers.")

args = sys.argv
data = args[1]
weights = valid_numbers(args[2])
impact = valid_operators(args[3])
output = args[4]

df = pd.read_csv('data.csv')
print("got the CSV file")
print("columns found✨: ")
print(df.columns.tolist())
if len(weights) == len(impact) and len(weights) == len(df.columns):
    pass
else:
    raise ValueError("Number of weights, operators, and columns do not match. ", len(weights), len(impact), len(df.columns))

run(df, weights, impact, output)