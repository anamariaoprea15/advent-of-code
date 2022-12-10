# Press the green button in the gutter to run the script.

# rock paper scissors
# A B C
# X Y Z
# A = X, A < Y, A > Z
# B > X, B = Y, B < Z
# C < X, C > Y, C = Z

# SCORE: 1 rock, 2 paper, 3 scissors
# SCORE2: 0 loss, 3 draw, 6 win
if __name__ == '__main__':
    if __name__ == '__main__':
        score = 0
        with open("input.txt") as fp:
            for line in fp:
                # print("Line{}: {}".format(count, line.strip().split()))
                round = line.strip().split()  # array with choice of both elves
                if round[0] == 'A':
                    if round[1] == 'X':  # tie
                        score += 3 + 1
                    if round[1] == 'Y':  # win with paper
                        score += 6 + 2
                    if round[1] == 'Z':  # loss with scissors
                        score += 0 + 3

                if round[0] == 'B':
                    if round[1] == 'X':  # loss with rock
                        score += 0 + 1
                    if round[1] == 'Y':  # draw with paper
                        score += 3 + 2
                    if round[1] == 'Z':  # win with scissors
                        score += 6 + 3

                if round[0] == 'C':
                    if round[1] == 'X':  # win with rock
                        score += 6 + 1
                    if round[1] == 'Y':  # loss with paper
                        score += 0 + 2
                    if round[1] == 'Z':  # tie with scissors
                        score += 3 + 3
        print(score)

        # mai simplu: o mapare intr-un dictionar pentru fiecare varianta
        score = 0
        options = {"A X": 3 + 1, "A Y": 6 + 2, "A Z": 0 + 3,
                   "B X": 0 + 1, "B Y": 3 + 2, "B Z": 6 + 3,
                   "C X": 6 + 1, "C Y": 0 + 2, "C Z": 3 + 3}
        with open("input.txt") as fp:
            for line in fp:
                score += options.get(line.strip())
        print(score)

        score = 0
        # NOW X = lose, Y = draw, Z = win
        options = {"A X": 0 + 3, "A Y": 3 + 1, "A Z": 6 + 2,
                   "B X": 0 + 1, "B Y": 3 + 2, "B Z": 6 + 3,
                   "C X": 0 + 2, "C Y": 3 + 3, "C Z": 6 + 1}
        with open("input.txt") as fp:
            for line in fp:
                score += options.get(line.strip())
        print(score)