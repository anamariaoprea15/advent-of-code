# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count = 0
    count2 = 0
    with open("input.txt") as fp:
        for line in fp:
            # print("Line{}: {}".format(count, line.strip()))
            pair = line.strip().split(",")
            print(pair)
            elf1 = pair[0].split("-")
            elf1 = [int(x) for x in elf1]
            elf2 = pair[1].split("-")
            elf2 = [int(x) for x in elf2]
            if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
                count += 1
            # part 2
            if elf1[0] <= elf2[0] <= elf1[1] or elf1[0] <= elf2[1] <= elf1[1] or elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]:
                count2 += 1
    print(count2)
