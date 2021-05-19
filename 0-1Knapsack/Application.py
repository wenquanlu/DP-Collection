from Algorithm import knapsack, knapsack_max
# use information given to fill in two lists
rate = []
weight = []
for i in range(5):
    rate.append(200)
    weight.append(20)
for i in range(5):
    rate.append(180)
    weight.append(15)
for i in range(10):
    rate.append(20)
    weight.append(5)
for i in range(5):
    rate.append(300)
    weight.append(25)
for i in range(5):
    rate.append(180)
    weight.append(22)

# find max rate achievable
max_rate = knapsack_max(rate, weight, 200)
print("the maximum rate of oxygen production is {} L/hr".format(max_rate))

# obtain binary list indicating inclusion of elements
result = knapsack(rate, weight, 200)

# print the elements out
for i in range(len(rate)):
    if result[i] == 1:
        print("{} ".format(weight[i]), end="")
print()