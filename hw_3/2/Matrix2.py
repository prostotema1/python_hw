import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class ArrayMixin(NDArrayOperatorsMixin):
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        args = [input_.data if isinstance(input_, Matrix) else input_ for input_ in inputs]
        result = getattr(ufunc, method)(*args, **kwargs)
        if isinstance(result, np.ndarray):
            return Matrix(result)
        else:
            return result

class IOOperationsMixin:
    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')

    def __str__(self):
        return str(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class Matrix(ArrayMixin, IOOperationsMixin):
    def __init__(self, data):
        self.data = data

np.random.seed(0)
data1 = np.random.randint(0, 10, (10, 10))
data2 = np.random.randint(0, 10, (10, 10))

matrix1 = Matrix(data1)
matrix2 = Matrix(data2)

matrix_add = matrix1 + matrix2
matrix_mul = matrix1 * matrix2
matrix_matmul = matrix1 @ matrix2

matrix_add.save_to_file("../artifacts/3_2/matrix+.txt")
matrix_mul.save_to_file("../artifacts/3_2/matrix''.txt")
matrix_matmul.save_to_file("../artifacts/3_2/matrix@.txt")
