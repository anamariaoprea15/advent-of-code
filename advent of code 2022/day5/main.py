# Press the green button in the gutter to run the script.
from collections import deque

if __name__ == '__main__':
    stack_info = []
    with open("input.txt") as fp:
        for line in fp:
            if line == "\n":
                break
            else:
                stack_info.append(line.strip())

    numbers = [int(x) for x in stack_info[-1].split("  ")]
    stack_info.pop()
    print(numbers)
    stacks = [deque() for i in range(numbers[-1])]
    print(len(stacks))

    for line in stack_info:
        line = line.split(" ")
        for i, el in enumerate(line):
            if el == "":
                line[i:] = line[i + 3:]
        for i, el in enumerate(line):
            if el != "":
                stacks[i].appendleft(el)
    for stack in stacks:
        print(stack)

    with open("input.txt") as fp:
        options = fp.read().strip().split("\n\n")[1]
    options = options.split("\n")
    for op in options:
        op = op.split(" ")
        quantity = int(op[1])
        from_stack = int(op[3])
        to_stack = int(op[5])
        little = deque()
        for i in range(quantity):
            aux = stacks[from_stack-1].pop()
            print(aux)
            # modified for part 2 of problem
            little.appendleft(aux)
        for aux in little:
            stacks[to_stack-1].append(aux)
    print("-----")
    for stack in stacks:
        print(stack[-1])
