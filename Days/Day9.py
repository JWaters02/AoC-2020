import fileinput
import time

start = time.time()
# Execution time: 3.28s
lines = [line.rstrip('\n') for line in fileinput.input("Day9Input.txt")]
lines = [int(i) for i in lines]

for i in range(25, len(lines)):
    previous_batch = lines[i-25:i]
    boolean = False
    for x in range(25):
        for y in range(25):
            if previous_batch[x] + previous_batch[y] == lines[i]:
                boolean = True
    if not boolean:
        terms = lines[i]

for i in range(len(lines)):
    for j in range(i + 2, len(lines)):
        result = lines[i:j]
        if sum(result) == terms:
            print(min(result) + max(result))

end = time.time()
print(f"Executiont time: {end - start}")