import time
import fileinput

start = time.time()

# Executation time: 0.115s
inputText = [line for line in fileinput.input("input.txt")]
inputText = "".join(inputText)
FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
passports = inputText.split('\n\n')

def validated_data(passport):
    valid = True
    for field in passport.split():
        key = field[:3]
        data = field[4:]
        if not valid:
            return valid

        if key == "byr": 
            valid = valid and len(data) == 4 and "1920" <= data <= "2002"
        elif key == "iyr": 
            valid = valid and len(data) == 4 and "2010" <= data <= "2020"
        elif key == "eyr": 
            valid = valid and len(data) == 4 and "2020" <= data <= "2030"
        elif key == "hgt": 
            valid = valid and validate_hgt(data)
        elif key == "hcl": 
            valid = valid and validate_hcl(data)
        elif key == "ecl": 
            FIELDS2 = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            valid = valid and data in FIELDS2
        elif key == "pid": 
            valid = valid and len(data) == 9 and data.isdigit() 
        else:
            continue
    return valid

def validate_hcl(data):
    try:
        int(data[1:], 16)
    except ValueError:
        return False
    return data[0] == "#"

def validate_hgt(height):
    if "cm" in height:
        return "150" <= height[:-2] <= "193"
    elif "in" in height:
        return "59" <= height[:-2] <= "76"
    return False

numFieldKeys = 0
numValidFields = 0
for passport in passports:
    fieldKeys = {field.split(":")[0] for field in passport.split()} 
    if fieldKeys and FIELDS == FIELDS:
        numFieldKeys += 1
        numValidFields += validated_data(passport)
    print(numValidFields)

end = time.time()
print(f"Executiont time: {end - start}")