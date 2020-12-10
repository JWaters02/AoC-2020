import fileinput
import time

combinationMemory = {}
def loopCombinations(first, last, adapter):
    current = (len(adapter), first)
    if current in combinationMemory:
        return combinationMemory[current]
    combinations = 0
    if last - first <= 3:
        combinations += 1
    if not adapter:
        return combinations
    if adapter[0] - first <= 3:
        combinations += loopCombinations(adapter[0], last, adapter[1:])
    combinations += loopCombinations(first, last, adapter[1:])
    combinationMemory[current] = combinations
    return combinations

def main():
    start = time.time()

    # Execution time: 0.06s
    lines = [line.rstrip('\n') for line in fileinput.input("Day10Input.txt")]
    lines = [int(i) for i in lines]
    print(loopCombinations(0, max(lines) + 3, sorted(lines)))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()