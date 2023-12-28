import csv
import io

EXAMPLE_INPUT = '''1,2
2,3
3,4
3,5
4,6'''

def load_graph(csv_string):
    graph_data = {}
    reader = csv.reader(io.StringIO(csv_string))
    for line in reader:
        node = line[0]
        edges = line[1:]
        graph_data.setdefault(node, []).extend(edges)
    return graph_data

def export_graph(m):
    res = io.StringIO()
    writer = csv.writer(res)
    for r in m:
        writer.writerow(r)
    return res.getvalue()


def extract_nodes(graph):
    nodes = set(graph.keys())
    for edges in graph.values():
        nodes.update(edges)
    return sorted(nodes), len(nodes)


def create_adjacency_matrix(graph, size):
    adj_matrix = [[0] * size for _ in range(size)]
    for node, edges in graph.items():
        node_index = int(node) - 1
        for edge in edges:
            edge_index = int(edge) - 1
            adj_matrix[node_index][edge_index] = 1
            adj_matrix[edge_index][node_index] = -1
    return adj_matrix


def analyze_graph(matrix):
    analysis = [[0] * 5 for _ in matrix]
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1:
                analysis[i][0] += 1
                analysis[i][2] += sum(1 for v in matrix[j] if v == 1)
            elif value == -1:
                analysis[i][1] += 1
                analysis[i][3] += sum(1 for v in matrix[j] if v == -1)
                analysis[i][4] += sum(1 for k, v in enumerate(matrix[j]) if v == 1 and k != i)
    return analysis


def save_to_csv(data, filename='result.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def task(csv):
    graph = load_graph(csv)
    _, size = extract_nodes(graph)
    adjacency_matrix = create_adjacency_matrix(graph, size)
    result_data = analyze_graph(adjacency_matrix)
    return export_graph(result_data)


if __name__ == '__main__':
    csv_input = EXAMPLE_INPUT
    result = task(csv_input)
    print(result)