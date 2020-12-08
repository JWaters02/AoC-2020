import time
import fileinput

def main():
    lines = [line for line in fileinput.input("Day8Input.txt")]

    for instructionSet in range(len(lines)):
        line_to_execute = lines[:]
        if line_to_execute[instructionSet].startswith('jmp'):
            line_to_execute[instructionSet] = line_to_execute[instructionSet].replace('jmp', 'nop')
        elif line_to_execute[instructionSet].startswith('nop'):
            line_to_execute[instructionSet] = line_to_execute[instructionSet].replace('nop', 'jmp')

        if part1(line_to_execute):
            print(part1(line_to_execute))

def part1(line_to_execute):
    while True:
        acc = 0
        pc = 0
        instructions_executed = set()
        
        while True:
            if pc == len(line_to_execute):
                return acc
            if pc in instructions_executed:
                return None
            instructions_executed.add(pc)
            instruction_type, arg = line_to_execute[pc].split()
            arg = int(arg)

            if instruction_type == 'jmp':
                pc += arg
                continue
            if instruction_type == 'acc':
                acc += arg
            if instruction_type == 'nop':
                pass
            pc += 1

start = time.time()
# Execution time: 0.17s
main()
end = time.time()
print(f"Executiont time: {end - start}")