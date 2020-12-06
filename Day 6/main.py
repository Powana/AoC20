with open("input.txt") as f:
    input_lines = f.readlines()


def part1():
    lines = [l[:-1] for l in input_lines]
    lines.append("")  # account for no newline at eof
    # lines = ["abc", "", "aaa", ""]
    chars = []
    n = 0

    for line in lines:
        if not line:
            n += len(chars)
            chars = []
        for c in line:
            if c not in chars:
                chars.append(c)

    return n


def part2():
    lines = [l[:-1] for l in input_lines]
    lines.append("")  # account for no newline at eof
    # lines = ["abc", "", "aaa", ""]
    chars = {}
    n = 0
    people = 0

    for line in lines:
        if not line:
            n += len([True for k, v in chars.items() if v == people])
            chars = {}
            people = 0
            continue
        for c in line:
            if c not in chars.keys():
                chars[c] = 1
            else:
                chars[c] += 1
        people += 1

    return n


if __name__ == "__main__":
    print(part1())
    print(part2())
