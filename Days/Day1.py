import itertools
import time

expenseReport = []
for i in range(200):
    expenseReport.append(int(input()))
start = time.time()

# Execution time: 4.32s
for i in range(len(expenseReport)):
    for j in range(len(expenseReport)):
        for k in range(len(expenseReport)):
            if (expenseReport[i] + expenseReport[j] + expenseReport[k]) == 2020:
                print(expenseReport[i] * expenseReport[j] * expenseReport[k])
                break
            
end = time.time()
print(f"Executiont time: {end - start}")

