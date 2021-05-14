"""
if j < s[i]   m[i][j] = m[i-1][j]
else: m[i][j] = m[i-1][j] or m[i-1][j - S[i]]
"""

def can_be_bi_partitioned(set):
    total = sum(set)
    if total % 2 == 1:
        return False
    half = int(total / 2)
    print(half)
    m = [[None for j in range(half + 1)] for i in range(len(set) + 1)]
    for j in range(1, half + 1):
        m[0][j] = False
    for i in range(len(set) + 1):
        m[i][0] = True
    for i in range(1, len(set) + 1):
        for j in range(1, half + 1):
            if j < set[i-1]:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = m[i-1][j] or m[i-1][j - set[i-1]]
    for i in range(len(set) + 1):
        for j in range(half + 1):
            print(m[i][j], " ", end="")
        print()

    return m[len(set)][half]

def find_bi_partition(set):
    total = sum(set)
    half = int(total / 2)
    print(half)
    m = [[None for j in range(half + 1)] for i in range(len(set) + 1)]
    for j in range(1, half + 1):
        m[0][j] = False
    for i in range(len(set) + 1):
        m[i][0] = True
    for i in range(1, len(set) + 1):
        for j in range(1, half + 1):
            if j < set[i-1]:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = m[i-1][j] or m[i-1][j - set[i-1]]
    row = len(set)
    col = half
    indices = []
    while row != 0:
        if m[row][col] == True:
            if m[row-1][col] == False:
                indices.append(row-1)
                col -= set[row - 1]
            else:
                row -= 1
    subset = []
    for i in indices:
        subset.append(set[i])
    return subset
