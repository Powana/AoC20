with open("test_input.txt") as f:
    input_lines = f.readlines()
lines = [int(x) for x in input_lines]


def part1():
    j = 0
    ones = 0
    threes = 0
    adapters = sorted(lines)
    for i in range(len(adapters)):
        dif = adapters[i] - j
        if dif > 3:
            return False, i, adapters[i]
        if dif == 1:
            ones += 1
        elif dif == 3:
            threes += 1
        j = adapters[i]

    j += 3
    threes += 1
    return ones * threes


# 1632 too low


def part2():
    j = 0
    n = 1
    adapters = sorted(lines)
    checked = []
    print(adapters)
    adapters.append(max(adapters) + 3)
    for i in range(len(adapters)):
        for ii in adapters[i + 1:i + 4]:
            dif = ii - adapters[i]
            if dif <= 3:
                if ii in checked:
                    n *= 2
                else:
                    checked.append(ii)


        j = adapters[i]

    return n


from math import factorial

# 70 368 744 177 664 too high


if __name__ == "__main__":
    print(part1())
    print(part2())
