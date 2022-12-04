import numpy as np
from numpy.linalg import eig
import math as m


class Matrix:
    def __init__(self, size, criteria):
        self.size = size
        self.criteria = criteria
        self.A = np.zeros((size, size))

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.A[i][j] == 0:
                    return False
        return True

    def to_vector(self):
        w, v = eig(self.A)

        vec = [x[0].real for x in v]
        norm = [x / sum(vec) for x in vec]
        return norm

    def put(self, crit1, crit2, val):
        self.A[self.criteria.index(crit1)][self.criteria.index(crit2)] = val
        self.A[self.criteria.index(crit2)][self.criteria.index(crit1)] = 1 / val

    def completer(self):
        length = len(self.A)
        g = np.zeros((length, length))

        for i in range(length):
            missing = 0
            for j in range(length):
                if self.A[i][j] == 0:
                    g[i][j] = 1
                    missing += 1

            g[i][i] = length - missing

        r = [0 for _ in range(length)]
        index = 0
        for i in range(length):
            temp = 0
            for j in range(length):
                if self.A[i][j] != 0:
                    temp += m.log(self.A[i][j])
            r[index] = temp
            index += 1

        w = [0 for _ in range(length)]
        index = 0
        for i in range(length):
            indey = 0
            for j in range(length):
                w[index] += r[indey] * g[i][j]
                indey += 1
            index += 1

        trueW = [m.exp(i) for i in w]

        divider = sum(w)
        finalW = [i / divider for i in trueW]

        out = np.zeros((length, length))

        indey = 0
        for i in range(length):
            index = 0
            for j in range(length):
                if self.A[i][j] == 0:
                    out[indey][index] = finalW[indey] / finalW[index]
                else:
                    out[indey][index] = self.A[i][j]
                index += 1
            indey += 1

        return out

    def __str__(self):
        return str(self.A)
