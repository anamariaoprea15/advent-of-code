# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    rocks = []

    with open("input.txt") as fp:

        text = fp.read().strip().split("\n")

        print(text)
        for path in text:
            steps = [tuple(map(int, step.split(","))) for step in path.split(" -> ")]
            # print(steps)
            for i, coord in enumerate(steps):
                if i == len(steps) - 1:
                    break
                dx = abs(steps[i][0] - steps[i + 1][0])
                dy = abs(steps[i][1] - steps[i + 1][1])
                # print(dx, dy)
                if steps[i][0] < steps[i + 1][0]:
                    for k in range(steps[i][0], steps[i + 1][0] + 1):
                        rocks.append((k, steps[i][1]))
                elif steps[i][0] > steps[i + 1][0]:
                    for k in range(steps[i + 1][0], steps[i][0] + 1):
                        rocks.append((k, steps[i][1]))

                if steps[i][1] < steps[i + 1][1]:
                    for k in range(steps[i][1], steps[i + 1][1] + 1):
                        rocks.append((steps[i][0], k))
                elif steps[i][1] > steps[i + 1][1]:
                    for k in range(steps[i + 1][1], steps[i][1] + 1):
                        rocks.append((steps[i][0], k))

    # print(rocks)
    rocks.append((500, 0))
    x_max = max(rocks, key=lambda i: i[0])[0]
    y_max = max(rocks, key=lambda i: i[1])[1]
    print(x_max, y_max)

    x_min = min(rocks, key=lambda i: i[0])[0]
    y_min = min(rocks, key=lambda i: i[1])[1]
    print(x_min, y_min)

    rocks.remove((500, 0))

    for j in range(y_min, y_max + 1):
        for i in range(x_min, x_max + 1):

            if (i, j) in rocks:
                print("#", end="")
            elif i == 500 and j == 0:
                print("+", end="")
            else:
                print(".", end="")
        print()

    x = 500
    y = 0
    sands = []
    ok = 1
    while True:
        x = 500
        y = 0
        while (x, y) not in rocks:
            if y > y_max:
                ok = 0
                break
            if (x, y + 1) not in rocks:
                y += 1
            elif (x - 1, y + 1) not in rocks:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in rocks:
                x += 1
                y += 1
            else:
                sands.append((x, y))
                rocks.append((x, y))
                break
        if ok == 0:
            break
print(len(sands))  # takes a few seconds :)
