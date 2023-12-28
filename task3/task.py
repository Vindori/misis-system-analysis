import csv
import argparse
import math

def load_matrix_from_file(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return [list(map(int, row)) for row in reader]

def calculate_normalized_matrix(relation_matrix):
    size = len(relation_matrix)
    normalized_matrix = [[float(cell) / (size - 1) for cell in row] for row in relation_matrix]
    return normalized_matrix

def calculate_row_entropy(normalized_row):
    return sum(-p * math.log2(p) for p in normalized_row if p > 0)

def calculate_total_entropy(normalized_matrix):
    return sum(calculate_row_entropy(row) for row in normalized_matrix)

def process_file(relation_matrix):
    normalized_matrix = calculate_normalized_matrix(relation_matrix)
    total_entropy = calculate_total_entropy(normalized_matrix)
    return total_entropy

if __name__ == '__main__':
    matrix = [
        [1,0,1,0,0],
        [1,1,2,0,0],
        [2,1,1,1,0],
        [1,1,0,1,1],
        [0,1,0,1,1],
        [0,1,0,1,0],
    ]
    entropy_result = process_file(matrix)
    print(f"Total Entropy: {entropy_result}")
