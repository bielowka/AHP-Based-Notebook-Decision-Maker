import numpy as np
from numpy.linalg import eig


def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n


def to_vector(A):
    w, v = eig(A)

    vec = [x[0].real for x in v]
    norm = [x / sum(vec) for x in vec]
    return norm


if __name__ == '__main__':
    a = np.array([[1, 2, 3],
                  [0.5, 1, 4],
                  [1 / 3, 0.25, 1]])
    print(to_vector(a))

    a = np.array([[1, 1 / 7, 1 / 5],
                  [7, 1, 3],
                  [5, 1 / 3, 1]])
    print(to_vector(a))
