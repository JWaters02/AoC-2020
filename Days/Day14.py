import fileinput
import time

def combinations(newIndex, floatingBits):
    if len(floatingBits) == 0:
        return [newIndex]
    else:
        return (combinations(newIndex, floatingBits[1:]) + combinations(newIndex + 2 ** floatingBits[0], floatingBits[1:]))

def markMem(lines):
    mask = ''
    memory = {}
    for line in lines:
        currentLine = line.strip()
        if currentLine.startswith('mask'):
            mask = line.split()[-1]
        else:
            assert len(mask) == 36
            index,_,currentValue = currentLine.split()
            newIndex = 0
            index = int(index.split('[')[-1][:-1])
            floatingBits = []
            currentValue = int(currentValue)
            reversedMask = reversed(mask)
            iList = [index]
            for element, bit in enumerate(reversedMask):
                if bit == '0':
                    newIndex += index & (2 ** element)
                elif bit == '1':
                    newIndex += (2 ** element)
                elif bit == 'X':
                    floatingBits.append(element)
                else:
                    assert False
            iList = combinations(newIndex, floatingBits)
            for i in iList:
                memory[i] = currentValue

    ret = 0
    for i, j in memory.items():
        ret += j
    return ret

def main():
    start = time.time()
    
    # Execution time: 0.3s
    lines = list(fileinput.input("Day14Input.txt"))
    print(markMem(lines))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()