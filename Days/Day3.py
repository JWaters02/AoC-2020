import time

inputLines = []
for i in range(323):
    inputLines.append(input())

start = time.time()
# Execution time: 0.001s
def get_collisions(lines, slope):
    collisions = 0
    columns, rows = len(lines[0]), len(lines)
    x, y = 0, 0

    while y < rows:
        if lines[y][x % columns] == '#':
            collisions = collisions + 1
        x, y = x + slope[0], y + slope[1]
    return collisions

output = get_collisions(inputLines, (1, 1)) * get_collisions(inputLines, (3, 1)) * get_collisions(inputLines, (5, 1)) * get_collisions(inputLines, (7, 1)) * get_collisions(inputLines, (1, 2))

print(str(output))
end = time.time()
print(f"Executiont time: {end - start}")