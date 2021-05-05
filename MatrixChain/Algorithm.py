import sys
"""
A0    *   A1    *    A2   *   A3
5 * 4    4 * 6     6 * 2     2 * 7
d0    d1       d2        d3      d4

M[i, j] = min{M[i, k] + M[k + 1, j] + di * dk+1 * dj+1}
"""


def matrix_chain_num_operations(dimensions):
    num_of_matrix = len(dimensions) - 1
    M = [[None for j in range(num_of_matrix)] for i in range(num_of_matrix)]
    N = [[None for j in range(num_of_matrix)] for i in range(num_of_matrix)]
    for i in range(num_of_matrix):
        M[i][i] = 0
    for b in range(1, num_of_matrix):
        for i in range(num_of_matrix - b):
            j = i + b
            M[i][j] = sys.maxsize
            for k in range(i, j):
                M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j + 1])
    return M[0][num_of_matrix - 1]


def matrix_chain_operation_sequence(dimensions):
    num_of_matrix = len(dimensions) - 1
    M = [[None for j in range(num_of_matrix)] for i in range(num_of_matrix)]
    N = [[None for j in range(num_of_matrix)] for i in range(num_of_matrix)]
    for i in range(num_of_matrix):
        M[i][i] = 0
    for b in range(1, num_of_matrix):
        for i in range(num_of_matrix - b):
            j = i + b
            M[i][j] = sys.maxsize
            k_set = -1
            for k in range(i, j):
                prev = M[i][j]
                M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j + 1])
                if prev != M[i][j]:
                    k_set = k
            N[i][j] = k_set

    i = 0
    j = num_of_matrix - 1
    def report(i, j, N):
        if abs(i - j) == 1:
            print(i, j, end = "")
            return
        elif i == j:
            print( i, end = "")
            return
        k = N[i][j]
        print("(", end = "")
        report(i, k, N)
        print(")", end = "")
        print("(", end = "")
        report(k+1, j, N)
        print(")", end = "")
    report(i, j, N)
    print()


