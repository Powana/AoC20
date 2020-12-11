from copy import deepcopy

with open("input.txt") as f:
    input_lines = f.readlines()

lines = [list(x[:-1]) for x in input_lines]


def apply_rules1(ls):
    ret_l = deepcopy(ls)
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            surr = [x for s in [
                (ls[i - 1][max(j - 1, 0):j + 2] if i != 0 else [1]) +
                (ls[i][j - 1:j]) +
                (ls[i][j + 1:j + 2]) +
                (ls[i + 1][max(j - 1, 0):j + 2] if i != len(ls) - 1 else [4])]
                    for x in s]
            c = surr.count("#")
            if ls[i][j] == "L" and c == 0:
                ret_l[i][j] = "#"
            elif ls[i][j] == "#" and c >= 4:
                ret_l[i][j] = "L"

    return ret_l


def occupied_in_dir(r):
    for x in r:
        if x == "#":
            return True
        if x == "L":
            return False
    return False


def look_vert(ls, i, j, down, log=False):
    start = i + 1 if down else max(i - 1, 0)
    end = None if down else (0 if i == 0 else None)
    d = 1 if down else -1
    rel_list = [a[j] for a in ls[start:end:d]]
    if log:
        print(rel_list, i, j, start, end)
    return occupied_in_dir(rel_list)


def look_hor(ls, i, j, right, log=False):
    start = j + 1 if right else max(j - 1, 0)
    end = None if right else (0 if j == 0 else None)
    dir = 1 if right else -1
    if log:
        print(start, end, dir, ls[i][start:end:dir])
    return occupied_in_dir(ls[i][start:end:dir])


def look_diags(ls, i, j):
    c = 0
    for i_d in [1, -1]:
        for j_d in [1, -1]:
            c += look_diag(ls, i, j, i_d, j_d)
    return c


def look_diag(ls, i, j, i_d, j_d):
    try:
        while True:
            i += i_d
            j += j_d
            if i < 0 or j < 0:
                return 0
            if ls[i][j] == "#":
                return 1
            if ls[i][j] == "L":
                return 0
    except IndexError:
        return 0


def apply_rules2(ls):
    ret_l = deepcopy(ls)
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            down = look_vert(ls, i, j, True)
            up = look_vert(ls, i, j, False)
            right = look_hor(ls, i, j, True)
            left = look_hor(ls, i, j, False)
            diags = look_diags(ls, i, j)
            c = diags + int(up) + int(down) + int(left) + int(right)
            if ls[i][j] == "L" and c == 0:
                ret_l[i][j] = "#"
            elif ls[i][j] == "#" and c >= 5:
                ret_l[i][j] = "L"

    return ret_l


def part1():
    before = deepcopy(lines)
    after = apply_rules1(before)

    while after != before:
        before = deepcopy(after)
        after = apply_rules1(before)

    return [x for s in after for x in s].count("#")


def part2():
    before = deepcopy(lines)
    after = apply_rules2(before)

    while after != before:
        before = deepcopy(after)
        after = apply_rules2(before)

    return [x for s in after for x in s].count("#")


if __name__ == "__main__":
    print(part1())
    print(part2())
