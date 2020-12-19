import fileinput
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

def checkAgainstCases(caseStrings, ruleStrings):
    validCases = 0
    for case in caseStrings:
        if generateCasesFromRules(0, case, ruleStrings):
            validCases += 1
    return validCases

def main():
    start = time.time()

    # Execution time: 210s
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

    print(checkAgainstCases(caseStrings, rulesStrings))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()