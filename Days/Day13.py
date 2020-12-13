import fileinput
import time

# Nicked from the internet :/
def chinese_remainder(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total

def getTable(lines):
    offsetsMatchingNums = []
    for schedule, ID in enumerate(lines[1].split(',')):
        if ID != 'x':
            ID = int(ID)
            offsetsMatchingNums.append((ID - schedule, ID))
        else:
            continue
    return chinese_remainder(offsetsMatchingNums)

def main():
    start = time.time()
    # Execution time: 0.06s
    lines = [line.rstrip('\n') for line in fileinput.input("Day13Input.txt")]
    print(getTable(lines))
    end = time.time()
    print(f"Executiont time: {end - start}")

main()