import fileinput
import time
import re

def parse(tokens):
    levelOfParenthesis = 0
    ret = []
    
    for token in tokens:
        if token == '(':
            levelOfParenthesis += 1
            ret.append(token)
        if token == ')':
            levelOfParenthesis -= 1
            ret.append(token)
            if levelOfParenthesis == 0:
                token = parse(ret[1:-1])
                ret = []
        if token not in '()':
            if levelOfParenthesis > 0:
                ret.append(token)
            else:
                values = reversePrecendence(token)
    return finalProduct(values)

def reversePrecendence(token):
    currentValue = None
    currentOperator = None
    if token == '*' or token == '+':
        currentOperator = token
    else:
        token = int(token)
        if currentValue == None:
            currentValue = [token]
        else:
            if currentOperator == '*':
                currentValue.append(token)
            else:
                currentValue[-1] += token
    return currentValue

def finalProduct(values):
    total = 1
    for i in values:
        total *= i
    return str(total)

def main():
    start = time.time()

    # Execution time: 
    lines = [line.rstrip('\n') for line in fileinput.input("Day18Input.txt")]
    # Nicked this regex from online LOL
    lines = [re.findall('\(|\d+|\*|\+|\)', line) for line in lines]
    for line in lines:
        result = [int(parse(line))]
    print(sum(result))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()