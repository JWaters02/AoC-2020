import itertools
import time

expenseReport = []
for i in range(200):
    expenseReport.append(int(input()))
start = time.time()

# Execution time: 4.32s
# for i in range(len(expenseReport)):
#     for j in range(len(expenseReport)):
#         for k in range(len(expenseReport)):
#             if (expenseReport[i] + expenseReport[j] + expenseReport[k]) == 2020:
#                 print(expenseReport[i] * expenseReport[j] * expenseReport[k])
#                 break

# Execution time: 0.9s
combinations = list(itertools.product(expenseReport, expenseReport, expenseReport))
for i in combinations:
    currentTuple = combinations[0][i]
    if currentTuple(0) + currentTuple(1) + currentTuple(2) == 2020:
        print(currentTuple(0) * currentTuple(1) * currentTuple(2))
        break

end = time.time()
print(f"Executiont time: {end - start}")

