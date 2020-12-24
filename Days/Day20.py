import fileinput
import time

def processTiles(raw):
    lines = raw.splitlines()
    id = int(lines[0][5:-1])
    data = lines[1:]
    return [id,data]

def getEdges(data):
    edges = [data[0],data[-1][::-1]]
    left = ''
    right = ''
    for line in data:
        left = line[0] + left
        right = right + line[-1]
    edges = edges + [left, right]
    return edges

def main():
    start = time.time()

    # Execution time: 0.06s
    lines = open('Day20Input.txt').read()
    lines = lines.split('\n\n')
    lines = lines[:-1]
    data = [processTiles(raw) for raw in lines]

    edgeData = {}
    matches = {}
    for tile in data:
        tileID = tile[0]
        matches[tileID] = 0
        edges = getEdges(tile[1])
        for edge in edges:
            other = None
            if edge in edgeData:
                other = edgeData[edge]
            else:
                reverse = edge[::-1]
                if reverse in edgeData:
                    other = edgeData[reverse]
                    edge = reverse
            if other is not None:
                matches[other] = matches[other] + 1
                matches[tileID] = matches[tileID] + 1
                edgeData[edge] = [other,tileID]
            else:
                edgeData[edge] = tileID
    acc = 1
    corners = []
    for tileID in matches:
        if matches[tileID] == 2:
            corners.append(tileID)
            acc = acc * tileID
    print(acc)

    end = time.time()
    print(f"Executiont time: {end - start}")

main()