import time

passwordList = []
for i in range(1000):
    passwordList.append(input())

start = time.time()
currentLine = []
firstPos = 0
secondPos = 0
letter = ''
password = ''
numValidPasswords = 0
for i in range(len(passwordList)): 
    currentLine = passwordList[i].split(' ')  
    rangeNumOfChars = currentLine[0].split('-')
    firstPos = int(rangeNumOfChars[0])
    secondPos = int(rangeNumOfChars[1])
    letter = currentLine[1]
    letter = letter.replace(":", "") 
    password = currentLine[2]

    # if letter appears in either firstpos or second pos
    if password[firstPos - 1] == letter or password[secondPos - 1] == letter:
        # if not letter appears in both firstpos and second pos (cancels out if both are there)
        if not (password[firstPos - 1] == letter and password[secondPos - 1] == letter):
            numValidPasswords += 1

end = time.time()
print(numValidPasswords)
print(f"Executiont time: {end - start}")