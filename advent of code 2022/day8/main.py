# Press the green button in the gutter to run the script.

def create_list_col(i, j, choice):
    list_col = []
    if choice == "up":
        for k in range(i):
            list_col.append(text[k][j])
    if choice == "down":
        for k in range(i + 1, len(text)):
            list_col.append(text[k][j])
    return list_col


def create_list_line(i, j, choice):
    list_line = []
    if choice == "left":
        for k in range(j):
            list_line.append(text[i][k])
    if choice == "right":
        for k in range(j + 1, len(text)):
            list_line.append(text[i][k])
    return list_line


def count_trees(i, j, choice, value):
    count = 0
    if choice == "left":
        for k in range(j - 1, -1, -1):
            if int(text[i][k]) >= value:
                count += 1
                break
            else:
                count += 1
    if choice == "right":
        for k in range(j + 1, len(text)):
            if int(text[i][k]) >= value:
                count += 1
                break
            else:
                count += 1

    if choice == "up":
        for k in range(i - 1, -1, -1):
            if int(text[k][j]) >= value:
                count += 1
                break
            else:
                count += 1

    if choice == "down":
        for k in range(i + 1, len(text)):
            if int(text[k][j]) >= value:
                count += 1
                break
            else:
                count += 1

    return count


if __name__ == '__main__':

    max_scenic = 0
    with open("input.txt") as fp:
        text = fp.read().strip()
    text = text.split("\n")
    print(text)
    count = 0
    for i in range(1, len(text) - 1):
        for j in range(1, len(text[i]) - 1):
            # for a[i][j]
            # compute max on line and max on column
            # max for a[1...i-1][j], a[i+1...n][j], a[i][1...j-1], a[i][j+1...n]
            list_line = create_list_line(i, j, "left")
            max_line_left = max(int(x) for x in list_line)
            list_line = create_list_line(i, j, "right")
            max_line_right = max(int(x) for x in list_line)

            list_col = create_list_col(i, j, "up")
            max_column_up = max(int(x) for x in list_col)
            list_col = create_list_col(i, j, "down")
            max_column_down = max(int(x) for x in list_col)
            if int(text[i][j]) > max_line_left or int(text[i][j]) > max_line_right or int(
                    text[i][j]) > max_column_up or int(text[i][j]) > max_column_down:
                count += 1

            # for every tree count how many are smaller
            scenic = count_trees(i, j, "left", int(text[i][j]))
            scenic *= count_trees(i, j, "right", int(text[i][j]))
            scenic *= count_trees(i, j, "up", int(text[i][j]))
            scenic *= count_trees(i, j, "down", int(text[i][j]))

            if scenic > max_scenic:
                max_scenic = scenic

    count += 2 * len(text)
    count += 2 * len(text[i])
    count -= 4  # delete duplicate corners

    print(count)
    print("max scenic = ", max_scenic)
