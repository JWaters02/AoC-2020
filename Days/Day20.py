import math
import time

def readTiles():
    tiles = {}
    with open("Day20Input.txt", "r") as file:
        for tile in file.read().split("\n\n"):
            name, *lines = tile.splitlines()
            num = int(name[5:-1])
            lines = [list(line) for line in lines]
            tiles[num] = lines
        return tiles

def getBorders(tile):
    return (tile[0], [element[-1] for element in tile], tile[-1], [element[0] for element in tile])

def getFlips(tile):
    return [tile, tile[::-1], [element[::-1] for element in tile], [element[::-1] for element in tile][::-1]]

def getRotations(tile):
    rotations = [tile]
    last = tile
    for _ in range(3):
        tile = [element[:] for element in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x])-y-1][x]
        last = tile
        rotations.append(tile)
    return rotations

def getTransforms(tile):
    possible = []
    for flip in getFlips(tile):
        possible.extend(getRotations(flip))
    output = []
    for position in possible:
        if position not in output:
            output.append(position)
    return output

def tilePicture(tiled, tileCombinations, dimension, x=0, y=0, seen=set()):
    if y == dimension:
        return tiled
    nextX = x + 1
    nextY = y
    if nextX == dimension:
        nextX = 0
        nextY += 1
    for tileID, tiles in tileCombinations.items():
        if tileID in seen:
            continue
        seen.add(tileID)
        for transId, border in tiles.items():
            top, temp, temp, left = border
            if x > 0:
                neighborId, neighborTrans = tiled[x-1][y]
                temp, neighborRight, temp, temp = tileCombinations[neighborId][neighborTrans]
                if neighborRight != left:
                    continue
            if y > 0:
                neighborId, neighborTrans = tiled[x][y-1]
                temp, temp, neighborBottom, temp = tileCombinations[neighborId][neighborTrans]
                if neighborBottom != top:
                    continue
            tiled[x][y] = (tileID, transId)
            ans = tilePicture(tiled, tileCombinations, dimension, x=nextX, y=nextY, seen=seen)
            if ans is not None:
                return ans
        seen.remove(tileID)
    tiled[x][y] = None
    return None

def getTiled(tiles):
    tileCombinations = {tileID: getTransforms(tile) for tileID, tile in tiles.items()}
    tileBorderCombinations = {}
    for tileID, tiles in tileCombinations.items():
        for index, tile in enumerate(tiles):
            if tileID not in tileBorderCombinations.keys():
                tileBorderCombinations[tileID] = {}
            tileBorderCombinations[tileID][index] = getBorders(tile)
    dimension = math.isqrt(len(tileCombinations))
    tiled = [[None] * dimension for _ in range(dimension)]
    return tileCombinations, tilePicture(tiled, tileBorderCombinations, dimension)

def removeGuides(tileCombinations, tiled):
    ret = []
    for row in tiled:
        tiles = []
        for num, transId in row:
            tile = tileCombinations[num][transId]
            tiles.append([element[1:-1] for element in tile[1:-1]])
        for y in range(len(tiles[0][0])):
            newRow = []
            for tileID in range(len(tiles)):
                newRow.extend(tiles[tileID][x][y] for x in range(len(tiles[tileID])))
            ret.append(newRow)
    return ret

def parseMonster():
    monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
    monsterLocations = []
    maxX, maxY = 0, 0
    for y, line in enumerate(monster.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                monsterLocations.append((x, y))
                maxX = max(x, maxX)
                maxY = max(y, maxY)
    return monsterLocations, maxX, maxY

def checkMonsters(grid):
    monsterLocations, maxX, maxY = parseMonster()
    monsterSpots = set()
    for y in range(len(grid)):
        if y + maxY >= len(grid):
            break
        for x in range(len(grid[y])):
            if x + maxX >= len(grid[y]):
                break
            isMonster = True
            for xOffset, yOffset in monsterLocations:
                if grid[y + yOffset][x + xOffset] != "#":
                    isMonster = False
                    break
            if isMonster:
                for dx, dy in monsterLocations:
                    monsterSpots.add((x + dx, y + dy))
    if len(monsterSpots) == 0:
        return None
    allFilled = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                allFilled.add((x, y))
    return len(allFilled - monsterSpots)

def part2(tileCombinations, tiled):
    grid = removeGuides(tileCombinations, tiled)
    gridCombinations = getTransforms(grid)
    for opt in gridCombinations:
        ret = checkMonsters(opt)
        if ret is not None: return ret

def main():
    start = time.time()

    # Execution time: 3s
    tiles = readTiles()
    tileCombinations, tiled = getTiled(tiles)
    print(part2(tileCombinations, tiled))
    
    end = time.time()
    print(f"Executiont time: {end - start}")


main()