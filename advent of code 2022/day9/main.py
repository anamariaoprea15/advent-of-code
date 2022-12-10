import numpy as np


# Press the green button in the gutter to run the script.
def make_move(head, tail):
    tail = list(tail)
    if abs(head[0] - tail[0]) > 1 and abs(head[1] - tail[1]) > 1:  # diagonal
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif abs(head[0] - tail[0]) > 1:  # left, right
        # can be replaced with sign
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        tail[1] = head[1]
    elif abs(head[1] - tail[1]) > 1:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
        tail[0] = head[0]

    return tuple(tail)


if __name__ == '__main__':

    # to do: make dict of values for directions
    direction_dict = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
    start = head = tail = (0, 0)
    visited_p1 = [(0, 0)]
    visited = [(0, 0)]
    # for part 2
    size = 10
    long_tail = [[0, 0] for _ in range(size-1)]

    with open("input.txt") as fp:
        for line in fp:
            direction, no_steps = line.strip().split(" ")
            for i in range(int(no_steps)):
                head = list(head)
                head[0] += direction_dict.get(direction)[0]
                head[1] += direction_dict.get(direction)[1]

                head = tuple(head)
                tail = make_move(head, tail)
                long_tail[0] = tail
                for k in range(1, size-1):
                    long_tail[k] = make_move(long_tail[k-1], long_tail[k])

                visited.append(tuple(long_tail[-1]))
                visited_p1.append(tuple(long_tail[0]))

    print(len(set(visited)))
    print(len(set(visited_p1)))
