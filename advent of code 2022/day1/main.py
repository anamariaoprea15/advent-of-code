# Press the green button in the gutter to run the script.
# The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc.
# that they've brought with them, one item per line.'
# Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.


# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
if __name__ == '__main__':
    count = 0
    countmax = 0
    calories = []
    with open("elves.txt") as fp:
        for line in fp:
            if line == '\n':
                if count > countmax:
                    countmax = count
                calories.append(count)
                count = 0
            else:
                count += int(line.strip())
            # print("Line{}: {}".format(count, line.strip()))
    calories.sort(reverse=True)
    # top 3 elves in total
    print(sum(calories[0:3]))
    # print(countmax)