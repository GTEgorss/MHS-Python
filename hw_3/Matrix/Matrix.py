import numpy as np

class Matrix:
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            if not all(len(row) == len(data[0]) for row in data):
                raise ValueError("All rows in the data must have the same number of columns.")
            data = np.array(data)

        if len(data.shape) != 2:
            raise ValueError("Data must be a 2D array or a list of lists.")
        self.data = data
        self.rows, self.cols = self.data.shape

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication.")

        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must equal the number of rows in the second matrix for matrix multiplication.")

        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __str__(self):
        return str(self.data)
