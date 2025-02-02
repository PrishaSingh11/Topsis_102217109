# -*- coding: utf-8 -*-
"""Topsis CLI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KhE9-QQPOIeU8aAL4nwfsI2NsbI8iheu
"""

import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    try:
        # Read the input file
        data = pd.read_csv(input_file)

        # Check input file structure
        if data.shape[1] < 3:
            raise ValueError("Input file must have at least three columns.")

        # decision matrix
        decision_matrix = data.iloc[:, 1:].values

        # All values in decision matrix are numeric
        if not np.issubdtype(decision_matrix.dtype, np.number):
            raise ValueError("All values from the second column onwards must be numeric.")

        # Check weights and impacts
        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')
        if len(weights) != decision_matrix.shape[1] or len(impacts) != decision_matrix.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of criteria.")
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Normalize the matrix
        norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

        # Apply weights
        weighted = norm_matrix * weights

        # Calculate ideal best and ideal worst
        ideal_best = [np.max(weighted[:, i]) if impacts[i] == '+' else np.min(weighted[:, i]) for i in range(len(impacts))]
        ideal_worst = [np.min(weighted[:, i]) if impacts[i] == '+' else np.max(weighted[:, i]) for i in range(len(impacts))]

        # Calculate distances to ideal best and worst
        dist_to_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
        dist_to_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

        # Calculate TOPSIS score
        topsis_score = dist_to_worst / (dist_to_best + dist_to_worst)

        # Rank alternatives
        data['Topsis Score'] = topsis_score
        data['Rank'] = topsis_score.argsort()[::-1] + 1

        # Save results to output file
        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    except FileNotFoundError:
        print("Input file not found. Please check the file path and try again.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, output_file = sys.argv
        topsis(input_file, weights, impacts, output_file)