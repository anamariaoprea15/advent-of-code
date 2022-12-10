if __name__ == '__main__':
    cycle = (20, 60, 100, 140, 180, 220)
    clock = 0
    x = 1
    sum = 0

    with open("input.txt") as fp:
        for line in fp:
            if line.startswith("noop"):
                clock += 1
                if clock in cycle:
                    sum += clock * x
                if (clock - 1) % 40 == 0:
                    print()
                if abs((clock - 1) % 40 - x) <= 1:  # in sprite
                    print("#", end="")
                else:
                    print(" ", end="")
            elif line.startswith("addx"):
                _, value = line.split(" ")
                clock += 1
                if clock in cycle:
                    sum += clock * x
                if (clock - 1) % 40 == 0:
                    print()
                if abs((clock - 1) % 40- x) <= 1:  # in sprite
                    print("#", end="")
                else:
                    print(" ", end="")
                clock += 1
                if clock in cycle:
                    sum += clock * x
                if (clock - 1) % 40 == 0:
                    print()
                if abs((clock - 1) % 40 - x) <= 1:  # in sprite
                    print("#", end="")
                else:
                    print(" ", end="")
                x += int(value)
    print(sum)


