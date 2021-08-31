class Matrix:
    def __init__(self, matrix_string):
        self._matrix_string = matrix_string
        self._matrix_by_row = self._map_matrix(matrix_string)
        self._matrix_by_col = self._transpose(self._matrix_by_row)

    def row(self, index):
        return self._matrix_by_row[index-1]

    def column(self, index):
        return self._matrix_by_col[index-1]

    def _map_matrix(self, matrix_string):
        row_strings = matrix_string.split('\n')
        matrix = map(lambda x: self._map_row(x), row_strings)
        return list(matrix)

    def _map_row(self, row_string):
        row_as_strs = row_string.split(' ')
        row_as_ints = map(lambda x: int(x), row_as_strs)
        return list(row_as_ints)

    def _transpose(self, matrix_by_row):
        transposed_matrix = map(list, zip(*matrix_by_row))
        return list(transposed_matrix)