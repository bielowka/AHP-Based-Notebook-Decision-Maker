import numpy as np


def Saaty_index(M):
    p_eigs = [x.real for x in np.linalg.eigvals(M)]
    p_eig = round(max(p_eigs), 3)
    return round((p_eig - len(M)) / (len(M) - 1), 3)


if __name__ == "__main__":
    M = [
        [1, 7, 1 / 6, 1 / 2, 1 / 4, 1 / 6, 4],
        [1 / 7, 1, 1 / 3, 5, 1 / 5, 1 / 7, 5],
        [6, 3, 1, 6, 3, 2, 8],
        [2, 1 / 5, 1 / 6, 1, 8, 1 / 5, 8],
        [4, 5, 1 / 3, 1 / 8, 1, 1 / 9, 2],
        [6, 7, 1 / 2, 5, 9, 1, 2],
        [1 / 4, 1 / 5, 1 / 8, 1 / 8, 1 / 2, 1 / 2, 1]
    ]

    M = np.array(M)
    print(Saaty_index(M))

    M = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]

    M = np.array(M)
    print(Saaty_index(M))

    M = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]

    M = np.array(M)
    print(Saaty_index(M))

    M = [
        [1, 2, 1, 1],
        [1 / 2, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]

    M = np.array(M)
    print(Saaty_index(M))

    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(Saaty_index(M))
