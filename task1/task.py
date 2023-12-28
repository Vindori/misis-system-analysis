import sys

def read_csv_cell(path, row, col):
    with open(path, 'r') as f:
        data = f.read().splitlines()
        if (len(data) < row) and (row > 0):
            raise IndexError('Index out of range')
        curr_row = data[row].split(',')
        if (len(curr_row) < col) and (col > 0):
            raise IndexError('Index out of range')
        return curr_row[col]


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: script.py <path> <row> <column>")
        sys.exit(1)

    filepath = sys.argv[1]
    row = int(sys.argv[2])
    col = int(sys.argv[3])

    val = read_csv_cell(filepath, row, col)
    print(val)