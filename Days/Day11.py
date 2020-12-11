import fileinput
import time


def lifeRound(lines):
    newGrid = []
    for row in range(len(lines)):
        replaceRow = ''
        for column in range(len(lines[0])):
            adjacentTiles = checkAdjacent(row, column, lines)
            if lines[row][column] == 'L' and '#' not in adjacentTiles:
                replaceRow += '#'
            elif lines[row][column] == '#' and adjacentTiles.count('#') >= 5:
                replaceRow += 'L'
            else:
                replaceRow += lines[row][column]
        newGrid.append(replaceRow)
    return newGrid

def checkAdjacent(row, column, lines):
    adjacentTiles = []
    for xAxis in (-1, 0, 1):
        for yAxis in (-1, 0, 1):
            if xAxis == yAxis == 0:
                continue
            count = 1
            while 0 <= row + (count * xAxis) < len(lines) and 0 <= column + (count * yAxis) < len(lines[0]):
                if lines[row + (count * xAxis)][column + (count * yAxis)] != '.':
                    adjacentTiles.append(lines[row + (count * xAxis)][column + (count * yAxis)])
                    break
                count += 1
    return adjacentTiles

def main():
    start = time.time()

    # Execution time: 11.5s
    lines = [line.rstrip('\n') for line in fileinput.input("Day11.txt")]
    currentLine = lines
    while True:
        after = lifeRound(currentLine)
        if after == currentLine:
            print(''.join(currentLine).count('#'))
            break
        currentLine = after

    end = time.time()
    print(f"Executiont time: {end - start}")

main()