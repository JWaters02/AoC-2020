import fileinput
import time
from collections import defaultdict

def takeSteps(position, step):
    x, y, z = position
    if step == 'ne': return (x + 1, y, z - 1)
    if step == 'e': return (x + 1, y - 1, z)
    if step == 'se': return (x, y - 1, z + 1)
    if step == 'sw': return (x - 1, y, z + 1)
    if step == 'w': return (x - 1, y + 1, z)
    if step == 'nw': return (x, y + 1, z - 1)

def flipTiles(lines):
    grid = defaultdict(bool)
    for line in lines:
        position = (0, 0, 0)
        while line:
            if line.startswith("n") or line.startswith("s"):
                direction = line[:2]
                line = line[2:]
                position = takeSteps(position, direction)
            else:
                direction = line[:1]
                line = line[1:]
                position = takeSteps(position, direction)
        grid[position] = not grid[position]
    print(countBlacks(grid))
    return grid

def livingArt(lines):
    grid = flipTiles(lines)
    directions = ["e", "w", "ne", "nw", "se", "sw"]
    for _ in range(100):
        positions = set()
        for position in grid.keys():
            positions.add(position)
            if grid[position]:
                for direction in directions:
                    positions.add(takeSteps(position, direction))
        newgrid = defaultdict(bool)
        for position in positions:
            count = sum([grid[takeSteps(position, direction)] for direction in directions])
            if grid[position]:
                if (count == 0 or count > 2):
                    newgrid[position] = False
                else:
                    newgrid[position] = True
            if not grid[position]:
                if count == 2:
                    newgrid[position] = True
                else:
                    newgrid[position] = False
        grid = newgrid
    return countBlacks(grid)

def countBlacks(grid):
    count = 0
    for v in grid.values():
        if v:
            count += 1
    return count

def main():
    start = time.time()

    # Execution time: 15.1s
    with open("Day24Input.txt") as file:
        lines = file.read().split("\n")
        lines = [line for line in lines if len(line) > 0]
    print(livingArt(lines))
    
    end = time.time()
    print(f"Executiont time: {end - start}")

main()