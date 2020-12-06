from math import floor, ceil

with open("input.txt") as f:
    input_lines = f.readlines()


def part1():
    bin_chars = [list(x)[:-1] for x in input_lines]
    # bin_chars = ["FBFBBFFRLR"]
    ids = []

    for cs in bin_chars:
        min_p = 0
        max_p = 128
        min_c = 0
        max_c = 8
        for c in cs:
            if c is "F":
                max_p -= ((max_p - min_p) / 2)
            elif c is "B":
                min_p += ((max_p - min_p) / 2)
            elif c is "L":
                max_c -= ((max_c - min_c) / 2)
            elif c is "R":
                min_c += (max_c - min_c) / 2

        ids.append(min_p * 8 + min_c)
    return ids


def part2():
    ids = part1()
    for i in ids:
        if i+1 not in ids and i+2 in ids:
            return i+1


if __name__ == "__main__":
    print(max(part1()))
    print(part2())
