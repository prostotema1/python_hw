import numpy as np

class Matrix:
    def __init__(self, data):
        self.data=data

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same dimensions for addition")

        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Incompatible dimensions for matrix multiplication")
        return Matrix(self.data @ other.data)

    def __str__(self):
        return str(self.data)

np.random.seed(0)
data1 = np.random.randint(0, 10, (10, 10))
data2 = np.random.randint(0, 10, (10, 10))

matrix1 = Matrix(data1)
matrix2 = Matrix(data2)

matrix_add = matrix1 + matrix2
matrix_mul = matrix1 * matrix2
matrix_matmul = matrix1 @ matrix2

np.savetxt("../artifacts/3_1/matrix+.txt", matrix_add.data, fmt='%d')
np.savetxt("../artifacts/3_1/matrix''.txt", matrix_mul.data, fmt='%d')
np.savetxt("../artifacts/3_1/matrix@.txt", matrix_matmul.data, fmt='%d')
