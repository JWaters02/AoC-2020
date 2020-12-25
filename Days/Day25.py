import fileinput

lines = [line.rstrip('\n') for line in fileinput.input("Day25Input.txt")]
a, b = [int(i) for i in lines]

def root(a):
    for i in range(100000000):
        if pow(7, i, 20201227) == a:
            return i

print(pow(a, root(b), 20201227))