def compare_packets(left, right):
    for l, r in zip(left, right):
        # print(l, r)
        if type(l) == list and type(r) == list:
            result = compare_packets(l, r)
            if result is not None:
                return result
        elif type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                pass
        elif type(l) == int and type(r) == list:
            result = compare_packets([l], r)
            if result is not None:
                return result
        elif type(l) == list and type(r) == int:
            result = compare_packets(l, [r])
            if result is not None:
                return result

    # in case of equality compare length of lists
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False


if __name__ == '__main__':
    i = 0
    packet = [0, 0]
    all_packets = [[[2]], [[6]]]
    pair_index = 1
    sum_pairs = 0
    with open("input.txt") as fp:
        text = fp.read().strip().split("\n\n")
        for packets in text:
            packets = packets.split("\n")
            left = eval(packets[0])
            right = eval(packets[1])
            all_packets.append(left)  # part 2
            all_packets.append(right)  # part 2
            # print(left, right)
            if compare_packets(left, right):
                # print(pair_index)
                sum_pairs += pair_index
            pair_index += 1

    print("result= ", sum_pairs)

    n = len(all_packets)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            swapped = True
            if not compare_packets(all_packets[j], all_packets[j + 1]):  # not sorted
                all_packets[j], all_packets[j + 1] = all_packets[j + 1], all_packets[j]
        if not swapped:
            break

    print((all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1))
