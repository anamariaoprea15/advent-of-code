if __name__ == '__main__':
    distinct = 4  # for part 1
    distinct = 14  # for part 2
    pos = -1
    with open("input.txt") as fp:
        text = fp.read().strip()
    for i, c in enumerate(text):
        if i >= len(text) - distinct:  # index out of bounds when searching 4 characters code
            break
        code = set(text[i:i + distinct])
        if len(code) == distinct:  # all characters are different
            pos = i + distinct
            break
    print(pos)
