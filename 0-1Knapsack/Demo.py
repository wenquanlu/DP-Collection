from Algorithm import knapsack

benefits = [4, 6, 2, 4, 1, 6, 1, 9]
weights =  [4, 8, 9, 5, 1, 8, 7, 2]
allocation = knapsack(benefits, weights, 15)
print(allocation)