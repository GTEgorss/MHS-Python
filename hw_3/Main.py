import numpy as np
from Matrix.Matrix import Matrix

np.random.seed(0)

if __name__ == "__main__":
    matrix1_data = np.random.randint(0, 10, (10, 10))
    matrix2_data = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    matrix_add = matrix1 + matrix2
    matrix_mult = matrix1 * matrix2
    matrix_product = matrix1 @ matrix2

    with open("artifacts/3.1/matrix+.txt", "w") as f:
        f.write(str(matrix_add))

    with open("artifacts/3.1/matrix*.txt", "w") as f:
        f.write(str(matrix_mult))

    with open("artifacts/3.1/matrix@.txt", "w") as f:
        f.write(str(matrix_product))
