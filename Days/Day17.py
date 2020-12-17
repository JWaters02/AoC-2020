import fileinput
import time

def lifeRound(grid):
    newGrid = {}
    for xAxis in range(min(x[0] for x in grid.keys()) - 1, max(x[0] for x in grid.keys()) + 2):
        for yAxis in range(min(y[1] for y in grid.keys()) - 1, max(y[1] for y in grid.keys()) + 2):
            for zAxis in range(min(z[2] for z in grid.keys()) - 1, max(z[2] for z in grid.keys()) + 2):
                for wAxis in range(min(w[3] for w in grid.keys()) - 1, max(w[3] for w in grid.keys()) + 2):
                    cube = grid.get((xAxis, yAxis, zAxis, wAxis), False)
                    neighbours = checkAdjacent(xAxis, yAxis, zAxis, wAxis, grid)
                    if (cube and neighbours in (2, 3)) or (not cube and neighbours == 3):
                        newGrid[(xAxis, yAxis, zAxis, wAxis)] = True
    return newGrid

def checkAdjacent(row, column, depth, w, grid):
    neighbours = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dw in (-1, 0, 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    if grid.get((row + dx, column + dy, depth + dz, w + dw), False):
                        neighbours += 1
    return neighbours

def setGrid(lines):
    grid = {}
    for row, line in enumerate(lines):
        for column, depth in enumerate(line):
            grid[(row, column, 0, 0)] = depth == '#'
    return grid

def main():
    start = time.time()

    # Execution time: 242.5s
    lines = [line.rstrip('\n') for line in fileinput.input("Day17Input.txt")]
    grid = setGrid(lines)

    for i in range(0, 6):
        grid = lifeRound(grid)
    print(sum(grid.values()))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()