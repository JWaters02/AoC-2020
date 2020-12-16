import fileinput
import time
from collections import defaultdict

def parseRules(rulesLines):
    ret = {}
    for i in rulesLines:
        currentRule, ranges = i.split(": ")
        rule1, rule2 = [[int(j) for j in rule.split("-")] for rule in ranges.split(" or ")]
        ret[currentRule] = (rule1, rule2)
    return ret

def parseYourTickets(yourTicketLine):
    ret = [int(j) for j in yourTicketLine.split(",")]
    return ret

def parseNearbyTickets(nearbyTicketsLines):
    ret = []
    for i in nearbyTicketsLines:
        ret.append([int(j) for j in i.split(",")])
    return ret

def getValidTickets(rules, nearbyTickets):
    validTickets = []
    errors = 0
    for ticket in nearbyTickets:
        currentTicketValid = True
        for currentValue in ticket:
            valid = False
            for i, ((lowRange1, highRange1), (lowRange2, highRange2)) in rules.items():
                if (lowRange1 <= currentValue <= highRange1) or (lowRange2 <= currentValue <= highRange2):
                    valid = True
            if not valid:
                errors += currentValue
                currentTicketValid = False
        if currentTicketValid:
            validTickets.append(ticket)
    return validTickets
    
def getValidPositions(rules, yourTickets, nearbyTickets):
    validTickets = getValidTickets(rules, nearbyTickets)
    validPositions = defaultdict(lambda: [])
    for field in range(len(yourTickets)):
        for rule, ((lowRange1, highRange1), (lowRange2, highRange2)) in rules.items():
            valid = True
            for ticket in validTickets:
                if not((lowRange1 <= ticket[field] <= highRange1) or (lowRange2 <= ticket[field] <= highRange2)):
                    valid = False
            if valid:
                validPositions[rule].append(field)
    return validPositions

def getProductOfValidTickets(validTicketPositions, yourTickets):
    rules = {}
    while len(rules.keys()) < len(yourTickets):
        for rule, valid in validTicketPositions.items():
            positions = valid[:]
            for i in rules.values():
                try:
                    positions.remove(i)
                except ValueError:
                    pass
            if len(positions) <= 1 and rule not in rules.keys():
                rules[rule] = positions[0]
    product = 1
    for key, value in rules.items():
        if key.startswith("departure"):
            product *= yourTickets[value]
    return product

def main():
    start = time.time()
    
    # Execution time: 0.6s
    lines = [line.rstrip('\n') for line in fileinput.input("Day16Input.txt")]
    rulesLines = []
    nearbyTicketsLines = []
    for i in range(0, 20):
        rulesLines.append(lines[i])
    for i in range(26, 266):
        nearbyTicketsLines.append(lines[i])

    rulesSanitised = parseRules(rulesLines)
    yourTickets = parseYourTickets(lines[22])
    nearbyTickets = parseNearbyTickets(nearbyTicketsLines)
    
    validTicketPositions = getValidPositions(rulesSanitised, yourTickets, nearbyTickets)
    print(getProductOfValidTickets(validTicketPositions, yourTickets))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()