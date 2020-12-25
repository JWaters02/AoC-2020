import time

start = time.time()
# Execution time: 38.3s
def root(a):
    for i in range(100000000):
        if pow(7, i, 20201227) == a: return i
print(pow(1614360, root(7734663), 20201227))
end = time.time()
print(f"Executiont time: {end - start}")