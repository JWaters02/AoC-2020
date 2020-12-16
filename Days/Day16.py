import fileinput
import time

def parseRules(rulesLines, i):
    ret = {}
    currentRule, ranges = i.split(": ")
    rule1, rule2 = [[int(i) for j in rule.split("-")] for rule in ranges.split(" or ")]
    ret[currentRule] = (rule1, rule2)
    return ret

def parseYourTickets(yourTicketLine, i):
    ret = []
    ret = [int(j) for j in i.split(",")]
    return ret

def parseNearbyTickets(nearbyTicketsLines, i):
    ret = []
    ret.append([int(j) for j in i.split(",")])
    return ret

def getErrors(rules, nearbyTickets):
    validTickets = []
    errors = 0
    for ticket in nearbyTickets:
        currentTicketValid = True
        for currentValue in ticket:
            valid = False
            for rule, ((lowRange1, highRange1), (lowRange2, highRange2)) in rules.items():
                if (lowRange1 <= currentValue <= highRange1) or (lowRange2 <= currentValue <= highRange2):
                    valid = True
            if not valid:
                errors += currentValue
                currentTicketValid = False
        if currentTicketValid:
            validTickets.append(ticket)
    return errors

def main():
    start = time.time()
    
    # Execution time: 0
    lines = [line.rstrip('\n') for line in fileinput.input("Day16Input.txt")]
    rulesLines = []
    nearbyTicketsLines = []
    lineNum = 0
    for i in lines:
        if i == '':
            lineNum += 1
        elif lineNum == 0:
            rulesSanitised = parseRules(rulesLines, i)
        elif lineNum == 1:
            lineNum += 1
        elif lineNum == 2:
            yourTickets = parseYourTickets(lines[23], i)
        elif lineNum == 3:
            lineNum += 1
        elif lineNum == 4:
            nearbyTickets = parseNearbyTickets(nearbyTicketsLines, i)
    
    print(getErrors(rulesSanitised, nearbyTickets))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()