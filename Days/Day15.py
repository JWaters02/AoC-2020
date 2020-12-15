import fileinput
import time
        
def main():
    start = time.time()
    
    # Execution time: 20s
    inputNums = '9,3,1,0,8,4'
    nums = list(map(int, inputNums.split(',')))
    dictNums = {
        n: i
        for i, n in enumerate(nums[:-1])
    }
    currentNum = nums[-1]
    for i in range(len(nums), 30000000):
        if currentNum in dictNums:
            newNum = i - dictNums[currentNum] - 1
        else:
            newNum = 0
        dictNums[currentNum] = i - 1
        currentNum = newNum
    print(currentNum)

    end = time.time()
    print(f"Executiont time: {end - start}")

main()