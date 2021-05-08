"""
                / B[k-1, w]   if wk > w
    B[k, w] = 
                \ max{B[k-1, w], B[k-1, w-wk] + bk}
"""

"""
S: benefits of n items
W: weight of n items
"""
def knapsack(S, W, max_weight):
    B = [[None for x in range(max_weight)] for y in range(len(W) + 1)]
    for i in range(max_weight):
        B[0][i] = 0
    for row in range(1, len(W) + 1):
        for w in range(max_weight):
            k = row - 1
            if W[k] > w:
                B[row][w] = B[row - 1][w]
            else:
                B[row][w] = max(B[row - 1][w], B[row-1][w - W[k]] + S[k])
    for i in range(len(B)):
        for j in range(len(B[0])):
            print("{} ".format(B[i][j]), end="")
        print()
    bit_result = [0 for x in range(len(W))]
    start_col = max_weight - 1
    start_row = len(W)
    max_profit = B[start_row][start_col]
    while start_row != 0:
        if (B[start_row - 1][start_col] != B[start_row][start_col]):
            bit_result[start_row -1] =1
            max_profit -= S[start_row - 1]
            start_row -= 1
            for i in range(max_weight):
                if (B[start_row][i] == max_profit):
                    start_col = i
        else:
            start_row -= 1
    return bit_result

"""
S = [4, 3, 1, 4, 5]
W = [2, 1, 4, 3, 8]

x = knapsack(S, W, 8)

print(x)
"""