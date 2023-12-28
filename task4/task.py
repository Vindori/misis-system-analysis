import math

def round_with_precision(num, precision=1):
    return round(num * 10**precision) / 10**precision

def create_sum_product_matrix():
    sum_values, product_values = list(), list()

    for a in range(1, 7):
        for b in range(1, 7):
            sum_values.append(a + b)
            product_values.append(a * b)

    sum_values, product_values = sorted(list(sum_values)), sorted(list(product_values))

    frequency_matrix = [[0] * len(product_values) for _ in sum_values]

    for i in range(1, 7):
        for j in range(1, 7):
            sum_ij = i + j
            product_ij = i * j
            frequency_matrix[sum_values.index(sum_ij)][product_values.index(product_ij)] += 1

    return frequency_matrix


def convert_to_probability_matrix(freq_matrix):
    total_pairs = 36
    return [[count / total_pairs for count in row] for row in freq_matrix]

def calculate_entropy_of_matrix(prob_matrix, axis='row'):
    entropy = 0.0
    
    if axis == 'row':
        for row in prob_matrix:
            row_prob = sum(row)
            if row_prob > 0:
                entropy += -row_prob * math.log2(row_prob)
    
    elif axis == 'column':
        for col in range(len(prob_matrix[0])):
            col_prob = sum(prob_matrix[row][col] for row in range(len(prob_matrix)))
            if col_prob > 0:
                entropy += -col_prob * math.log2(col_prob)

    return entropy

def calculate_joint_entropy_of_matrix(matrix):
    return -sum(p * math.log2(p) for row in matrix for p in row if p > 0)

def calculate_conditional_entropy(freq_matrix, prob_matrix):
    conditional_entropy = 0.0

    for row_idx, row in enumerate(freq_matrix):
        row_total = sum(row)
        for col_idx, count in enumerate(row):
            if count > 0:
                p = prob_matrix[row_idx][col_idx]
                conditional_entropy += -p * math.log2(p / (row_total / 36))

    return conditional_entropy

def task():
    freq_matrix = create_sum_product_matrix()
    prob_matrix = convert_to_probability_matrix(freq_matrix)

    entropy_row = calculate_entropy_of_matrix(prob_matrix, axis='row')
    entropy_col = calculate_entropy_of_matrix(prob_matrix, axis='column')
    joint_entropy = calculate_joint_entropy_of_matrix(prob_matrix)
    conditional_entropy = calculate_conditional_entropy(freq_matrix, prob_matrix)

    mutual_information = entropy_col - conditional_entropy
    
    return entropy_row, entropy_col, joint_entropy, conditional_entropy, mutual_information

if __name__ == '__main__':
    entropy_results = task()
    print(entropy_results)
