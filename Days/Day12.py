import fileinput
import time

def takeSteps(lines):
    xDistance, yDistance, xWaypoint, yWaypoint = 0, 0, 10, 1
    for line in lines:
        operation = line[:1]
        distanceOrHeading = int(line[1:])
        if operation == 'F':
            xDistance += xWaypoint * distanceOrHeading
            yDistance += yWaypoint * distanceOrHeading
        elif operation == 'N':
            yWaypoint += distanceOrHeading
        elif operation == 'S':
            yWaypoint -= distanceOrHeading
        elif operation == 'E':
            xWaypoint += distanceOrHeading
        elif operation == 'W':
            xWaypoint -= distanceOrHeading
        elif operation == 'L':
            while distanceOrHeading:
                distanceOrHeading -= 90
                xWaypoint, yWaypoint = rotateWaypoint(xWaypoint, yWaypoint, operation)
        elif operation == 'R':
            while distanceOrHeading:
                distanceOrHeading -= 90
                xWaypoint, yWaypoint = rotateWaypoint(xWaypoint, yWaypoint, operation)
    return getManhattenDistance(xDistance, yDistance)

def rotateWaypoint(xWaypoint, yWaypoint, rotateDirection):
    if rotateDirection == 'L':
        return -yWaypoint, xWaypoint
    elif rotateDirection == 'R':
        return yWaypoint, -xWaypoint

def getManhattenDistance(xDistance, yDistance):
    return abs(xDistance) + abs(yDistance)

def main():
    start = time.time()
    # Execution time: 0.05s
    lines = [line.rstrip('\n') for line in fileinput.input("Day12Input.txt")]
    distance =  takeSteps(lines)
    print(distance)
    end = time.time()
    print(f"Executiont time: {end - start}")

main()