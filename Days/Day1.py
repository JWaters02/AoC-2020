import itertools

expenseReport = []
for i in range(200):
    expenseReport.append(int(input()))

# for i in range(len(expenseReport)):
#     for j in range(len(expenseReport)):
#         for k in range(len(expenseReport)):
#             if (expenseReport[i] + expenseReport[j] + expenseReport[k]) == 2020:
#                 print(expenseReport[i] * expenseReport[j] * expenseReport[k])
#                 break

combinations = [()]
combinations = list(itertools.product(expenseReport, expenseReport, expenseReport))
for i in combinations:
    currentTuple = ()
    currentTuple = combinations[i]
    if currentTuple(0) + currentTuple(1) + currentTuple(2) == 2020:
        print(currentTuple(0) * currentTuple(1) * currentTuple(2))
        break

