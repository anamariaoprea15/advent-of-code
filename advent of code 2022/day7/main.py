if __name__ == '__main__':

    DISK_SPACE = 70000000
    REQUIRED_SPACE = 30000000
    with open("input.txt") as fp:
        text = fp.read().split("\n")

    path = []
    directories = {}
    for command in text:
        command = command.split(" ")
        # print(command)
        if command[0] == "$":  # is a command
            if command[1] == "cd":
                if command[2] == "/":
                    path = ["/"]
                elif command[2] == "..":
                    del path[-1]
                else:
                    path.append(command[2])
        else:
            if command[0] != "dir":
                for i in range(len(path)):
                    path_key = "/" + "/".join(path[1:i + 1])
                    directories.setdefault(path_key, 0)
                    directories[path_key] += int(command[0])

    print(directories)
    result = 0
    for size in directories.values():
        if size <= 100000:
            result += size
    print("result = ", result)

    unused_space = DISK_SPACE - directories.get("/")
    print(unused_space)
    minimum_path = ""
    min_size = REQUIRED_SPACE
    if unused_space < REQUIRED_SPACE:
        for path, size in directories.items():
            if size >= REQUIRED_SPACE - unused_space and size < min_size:
                min_size = size
                minimum_path = path
    print(min_size)
