import fileinput
import itertools
import time

class Food:
    def __init__(self, s):
        self.ingredients = s[:s.index("(")].strip().split(" ")
        self.allergens = s[s.index("(contains") + len("(contains"):-1].strip().split(", ")

def generateAllergies(foods):
    allIngredients = set()
    allergyDict = {}
    for food in foods:
        allIngredients = allIngredients.union(set(food.ingredients))
        for allergen in food.allergens:
            if not allergen in allergyDict:
                allergyDict[allergen] = set(food.ingredients)
            else:
                allergyDict[allergen] = allergyDict[allergen].intersection(food.ingredients)
    notAllergyIngredients = generateNotAllergyIngredients(allergyDict, allIngredients)
    safeFoods = countSafeFoods(food, notAllergyIngredients)
    print(safeFoods)
    return allergyDict

def generateNotAllergyIngredients(allergyDict, allIngredients):
    allergyIngredients = set()
    for k in allergyDict:
        allergyIngredients = allergyIngredients.union(allergyDict[k])
    notAllergyIngredients = allIngredients.difference(allergyIngredients)
    return notAllergyIngredients

def countSafeFoods(foods, notAllergyIngredients):
    count = 0
    for food in foods:
        for ingredient in food.ingredients:
            if ingredient in notAllergyIngredients:
                count += 1
    return count

def generateDangerousIngredients(allergyDict):
    out = []
    while len(allergyDict) > 0:
        a = None
        remove = None
        for a in allergyDict:
            if len(allergyDict[a]) == 1:
                remove = allergyDict[a].pop()
                out.append((a, remove))
                break
        if remove == None:
            break
        del allergyDict[a]
        for b in allergyDict:
            if remove in allergyDict[b]:
                allergyDict[b].remove(remove)
    return out

def main():
    start = time.time()

    # Execution time: 0.02s
    lines = [line.rstrip('\n') for line in fileinput.input("Day21Input.txt")]
    foods = list(map(Food, lines))
    
    allergyDict = generateAllergies(foods)
    print(",".join(list(map(lambda x: x[1], sorted(generateDangerousIngredients(allergyDict))))))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()
