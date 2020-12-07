import fileinput
import time

def main():
    rules = {}
    start = time.time()

    # Execution time 0.06s
    for line in fileinput.input("day7input.txt"):
        masterBag = line.split(" contain ")[0].split(" bag")[0]
        text = line.split(" contain ")[1].split(", ")
        stupidBag = []
        for bag in text:
            try:
                stupidBag.append([int(bag[0]), bag[2:].split(" bag")[0]])
            except ValueError:
                continue
        rules[masterBag] = stupidBag
    solution = insiderBags("shiny gold", rules)
    print(solution)
    end = time.time()
    print(f"Executiont time: {end - start}")

def insiderBags(masterBag, rules):
    count = 0
    for rule in rules[masterBag]:
        count += rule[0] * insiderBags(rule[1], rules) + rule[0]
    return count

main()