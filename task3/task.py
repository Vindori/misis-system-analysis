import io
import csv
import math

EXAMPLE_INPUT = '''1,0,1,0,0
1,1,2,0,0
2,1,1,1,0
1,1,0,1,1
0,1,0,1,1
0,1,0,1,0'''

def round_with_precision(num, precision=1):
    return round(num * 10**precision) / 10**precision

def load_matrix_from_string(csv_string):
    reader = csv.reader(io.StringIO(csv_string))
    return [list(map(int, row)) for row in reader]

def calculate_normalized_matrix(relation_matrix):
    size = len(relation_matrix)
    normalized_matrix = [[float(cell) / (size - 1) for cell in row] for row in relation_matrix]
    return normalized_matrix

def calculate_row_entropy(normalized_row):
    return sum(-p * math.log2(p) for p in normalized_row if p > 0)

def calculate_total_entropy(normalized_matrix):
    return sum(calculate_row_entropy(row) for row in normalized_matrix)

def task(matrix_csv):
    relation_matrix = load_matrix_from_string(matrix_csv)
    normalized_matrix = calculate_normalized_matrix(relation_matrix)
    total_entropy = calculate_total_entropy(normalized_matrix)
    return total_entropy

if __name__ == '__main__':
    matrix_s = EXAMPLE_INPUT
    entropy_result = task(matrix_s)
    print(entropy_result)
