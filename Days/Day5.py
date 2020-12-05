import time

lines = []
for i in range(897):
    lines.append(input())

start = time.time()

# Execution time: 0.002s
seats = set()
for line in lines:
    line = line.replace('F', '0')
    line = line.replace('B', '1')
    line = line.replace('L', '0')
    line = line.replace('R', '1')
    num = int(line, 2)
    seats.add(num)

for i in range(256 * 8):
    if (i not in seats):
        if i + 1 in seats:
            if i - 1 in seats:
                print(i)

end = time.time()
print(f"Executiont time: {end - start}")