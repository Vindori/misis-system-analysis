def read_csv_line(path, row, col):
    with open(path, 'r') as f:
        data = f.read().splitlines()
        if (len(data) < row) and (row > 0):
            raise IndexError('Index out of range')
        curr_row = data[row].split(',')
        if (len(curr_row) < col) and (col > 0):
            raise IndexError('Index out of range')
        return curr_row[col]


if __name__ == '__main__':
    print(read_csv_line('example.csv', 4, 5))