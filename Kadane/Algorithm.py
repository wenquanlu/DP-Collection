import sys
"""
Given an array, find the max sum of a subarray
local_max = max(A[i], A[i] + local_max)
"""
def max_sum_subarray(array):
    local_max = 0
    global_max = -sys.maxsize - 1
    for i in range(len(array)):
        local_max = max(array[i], array[i] + local_max)
        if (local_max > global_max):
            global_max = local_max
    return global_max