import numpy as np


class HashMixin:
    def __init__(self, data):
        self.data = data

    def __hash__(self):
        # Simple hash function: sum of elements modulo 10
        return int(self.data.sum()) % 10


class Matrix(HashMixin):

    def __matmul__(self, other):
        return Matrix(self.data @ other.data)

    def __hash__(self):
        return HashMixin.__hash__(self)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')


cache = {}


def cached_matmul(a, b):
    key = (hash(a), hash(b))
    if key in cache:
        print(f"Cache hit for key {key}")
        return cache[key]
    else:
        print(f"Cache miss for key {key}")
        result = a @ b
        cache[key] = result
        return result


A_data = np.array([[1, 1],
                   [1, 2]])
C_data = np.array([[2, 0],
                   [0, 3]])

A = Matrix(A_data)
C = Matrix(C_data)

B_data = np.array([[1, 0],
                   [0, 1]])
B = Matrix(B_data)
D = Matrix(B_data.copy())

assert hash(A) == hash(C)
assert A != C
assert B == D

AB = cached_matmul(A, B)

CD = cached_matmul(C, D)

A.save_to_file("../artifacts/3_3/A.txt")
B.save_to_file("../artifacts/3_3/B.txt")
C.save_to_file("../artifacts/3_3/C.txt")
D.save_to_file("../artifacts/3_3/D.txt")
AB.save_to_file("../artifacts/3_3/AB.txt")
CD.save_to_file("../artifacts/3_3/CD.txt")

with open("../artifacts/3_3/hash.txt", "w") as f:
    f.write(f"hash(AB): {hash(AB)}\n")
    f.write(f"hash(CD): {hash(CD)}\n")

