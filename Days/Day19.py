import fileinput
import itertools
import time

def generateCasesFromRules(ruleNumber, case, ruleStrings):
    validRules = {}
    if type(ruleStrings[ruleNumber]) is str:
        return case == ruleStrings[ruleNumber]
    if (ruleNumber, case) not in validRules:
        for i in range(1, len(case) + 1):
            leftLeftRule, leftRightRule = case[:i], case[i:]
            for j in ruleStrings[ruleNumber]:
                if len(j) == 1:
                    if generateCasesFromRules(j[0], case, ruleStrings):
                        validRules[ruleNumber, case] = True
                        return True
                else:
                    leftRightRule, rightRightRule = j
                    if generateCasesFromRules(leftRightRule, leftLeftRule, ruleStrings) and generateCasesFromRules(rightRightRule, leftRightRule, ruleStrings):
                        validRules[ruleNumber, case] = True
                        return True
        validRules[ruleNumber, case] = False
    return validRules[ruleNumber, case]

def generateNewCasesFromNewRules(ruleNumber, ruleStrings):
    rulePos = {}
    if ruleNumber in rulePos:
        return rulePos[ruleNumber]
    if type(ruleStrings[ruleNumber]) is str:
        rulePos[ruleNumber] = [ruleStrings[ruleNumber]]
        return rulePos[ruleNumber]
    rulePos[ruleNumber] = []
    for vd in ruleStrings[ruleNumber]:
        rulePos[ruleNumber].extend([''.join(newLine) for newLine in itertools.product(*[generateNewCasesFromNewRules(newRule, ruleStrings) for newRule in vd])])
    return rulePos[ruleNumber]

def handleLoopingRules(ruleStrings, caseStrings):
    rule42 = generateNewCasesFromNewRules(42, ruleStrings)
    rule31 = generateNewCasesFromNewRules(31, ruleStrings)
    count = 0
    for case in caseStrings:
        if len(case) % 8 != 0:
            continue
        bc = [case[i:i + 8] for i in range(0, len(case), 8)]
        difference = 0
        case42 = 0
        while difference < len(bc) and bc[difference] in rule42:
            difference += 1
            case42 += 1
        case31 = 0
        while difference < len(bc) and bc[difference] in rule31:
            difference += 1
            case31 += 1
        if difference == len(bc) and case31 < case42 and case31 > 0:
            count += 1
    return count

def main():
    start = time.time()

    # Execution time: 0.02s
    with open("Day19Input.txt") as line:
        lines = line.read().strip("\n")
    rules, cases = lines.split("\n\n")
    rules = rules.split("\n")
    caseStrings = cases.split("\n")
    rulesStrings = {}
    for line in rules:
        leftRules, rightRules = line.split(": ")
        rightRules = rightRules.split(" | ")
        if '"' in line:
            rulesStrings[int(leftRules)] = rightRules[0].strip('"')
        else:
            rulesStrings[int(leftRules)] = [[int(rulePointer) for rulePointer in rule.split(" ")] for rule in rightRules]
    print(handleLoopingRules(rulesStrings, caseStrings))
    
    end = time.time()
    print(f"Executiont time: {end - start}")

main()