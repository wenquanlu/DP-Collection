from Algorithm import matrix_chain_num_operations, matrix_chain_operation_sequence

dimensions = [5, 4, 6, 2, 7]
print(matrix_chain_num_operations(dimensions))
matrix_chain_operation_sequence(dimensions)

"""

"""

dimensions2 = [3, 4, 1, 2, 6, 3, 8]
print(matrix_chain_num_operations(dimensions2))
matrix_chain_operation_sequence(dimensions2)

"""
3*4 4*1 1*2 2*6 6*3 3*8

(3 * 4 * 1) + (((1 * 2 * 6) + (1 * 6 * 3) + (1 * 3 * 8))) + (3 * 1 * 8) = 90
"""