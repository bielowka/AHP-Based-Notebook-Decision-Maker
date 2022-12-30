import numpy as np


def Saaty_index(M):
    p_eig = np.linalg.eigvals(M)[0]
    return (p_eig - len(M)) / (len(M) - 1)


if __name__ == "__main__":
    M = [
        [1, 7, 1/6, 1/2, 1/4, 1/6, 4],
        [1/7, 1, 1/3, 5, 1/5, 1/7, 5],
        [6, 3, 1, 6, 3, 2, 8],
        [2, 1/5, 1/6, 1, 8, 1/5, 8],
        [4, 5, 1/3, 1/8, 1, 1/9, 2],
        [6, 7, 1/2, 5, 9, 1, 2],
        [1/4, 1/5, 1/8, 1/8, 1/2, 1/2, 1]
        ]

    M = np.array(M)
    print(Saaty_index(M))