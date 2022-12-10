if __name__ == '__main__':
    count = 0
    score = 0
    with open("input.txt") as fp:
        for line in fp:
            # print("Line{}: {}".format(count, line.strip()))
            items = line.strip()
            middle = len(items) // 2
            s1 = items[0:middle]
            s2 = items[middle:]

            a = list(set(s1) & set(s2))
            if a[0].islower():
                score += ord(a[0]) - 96
            if a[0].isupper():
                score += ord(a[0]) - 38
    print(score)

    group = 0
    lines = []
    sum_badges = 0
    with open("input.txt") as fp:
        for line in fp:
            group += 1
            lines.append(line.strip())
            if group == 3: # go to new group
                # first find common badge
                a = list(set(lines[0]) & set(lines[1]) & set(lines[2]))

                print(a[0])
                if a[0].islower():
                    sum_badges += ord(a[0]) - 96
                if a[0].isupper():
                    sum_badges += ord(a[0]) - 38
                lines = []
                group = 0
            # print("Line{}: {}".format(count, line.strip()))

    print(sum_badges)
