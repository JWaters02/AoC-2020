import time
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def game(lines):
    nodes, previous_node = {}, None
    for i in lines:
        node = Node(i)
        nodes[i] = node
        if previous_node is not None:
            previous_node.right = node
            node.left = previous_node
        previous_node = node

    for i in range(len(lines) + 1, 1000001):
        node = Node(i)
        nodes[i] = node
        if previous_node is not None:
            previous_node.right = node
            node.left = previous_node
        previous_node = node

    pointer = nodes[lines[0]]
    previous_node.right = pointer
    pointer.left = previous_node

    assert len(nodes) == 1000000
    pointer = nodes[lines[0]]
    for i in range(10000000):
        if i % 250000 == 0:
            print(i)
        pointer_value = pointer.value

        cup1 = pointer.right
        cup2 = cup1.right
        cup3 = cup2.right
        
        pointer.right = cup3.right
        pointer.right.left = pointer

        dynamic_value = pointer_value - 1 or 1000000
        while dynamic_value in (cup1.value, cup2.value, cup3.value):
            dynamic_value = dynamic_value - 1 or 1000000

        dynamic_node = nodes[dynamic_value]
        cup3.right = dynamic_node.right
        cup3.right.left = cup3
        dynamic_node.right = cup1
        cup1.left = dynamic_node

        pointer = pointer.right
    while pointer.value != 1:
        pointer = pointer.right
    return pointer.right.value * pointer.right.right.value

def main():
    start = time.time()

    # Execution time:
    with open("Day23Input.txt") as line:
        lines = [int(i) for i in line.read().strip()]
    print(game(lines))

    end = time.time()
    print(f"Executiont time: {end - start}")

main()