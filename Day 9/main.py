with open("input.txt") as f:
    input_lines = f.readlines()

lines = [int(l) for l in input_lines]
n_pre = 25


def part1():
    for i, n in enumerate(lines):
        if i >= n_pre:
            pre_lines = lines[i-n_pre:i+1]
            sum_exists = False
            for j in pre_lines:
                for jj in pre_lines:
                    if j + jj == n:
                        sum_exists = True
            if not sum_exists:
                return n


def part2():
    invalid_n = part1()
    for x in range(len(lines)):
        for y in range(1, len(lines) - x):
            if len(lines[x:y]) > 1 and sum(lines[x:y]) == invalid_n:
                if lines[x] != lines[y]:
                    return min(lines[x:y]) + max(lines[x:y])


# 3607989 too high
# 3546087 too high

if __name__ == "__main__":
    print(part1())
    print(part2())
