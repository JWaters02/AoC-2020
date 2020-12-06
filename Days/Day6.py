import time
import string
import fileinput

start = time.time()

# Execution time: 0.04s
inputText = [line for line in fileinput.input("Day6Input.txt")]
inputText = "".join(inputText)
lines = inputText.split("\n\n")
count = 0
alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)
for x in lines:
    current_line = x.split("\n")
    for question in alphabet:
        if all([question in y for y in current_line]):
            count += 1
print(count)

end = time.time()
print(f"Executiont time: {end - start}")