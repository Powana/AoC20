with open("input.txt") as f:
    input_lines = f.readlines()

accumulator = 0
i = 0


def acc(n):
    global accumulator, i
    accumulator += n
    i += 1


def jump(n):
    global i
    i += n


def noc(n):
    global i
    i += 1


funcs = {"acc": acc, "jmp": jump, "nop": noc}
lines = [str(li.strip()).split() for li in input_lines]
lines = [[x[0], int(x[1][1:]) * (1 if x[1][0] is "+" else -1)] for x in lines]


def part1():
    run_is = []

    while True:
        if i in run_is:
            return accumulator
        run_is.append(i)
        l = lines[i]
        funcs[l[0]](l[1])


def part2():
    global accumulator, i, lines

    for idx, line in enumerate(lines):
        i = 0
        accumulator = 0
        run_is = []
        cmd = line[0]
        if cmd == "nop":
            lines[idx][0] = "jmp"
        elif cmd == "jmp":
            lines[idx][0] = "nop"
        if cmd in ["jmp", "nop"]:
            while True:
                if i in run_is:
                    print(i, "already seen")
                    break
                if i == len(lines):
                    return accumulator
                run_is.append(i)
                l = lines[i]
                funcs[l[0]](l[1])
        lines[idx][0] = cmd


# 4274 too high


if __name__ == "__main__":
    # print(part1())
    print(part2())
