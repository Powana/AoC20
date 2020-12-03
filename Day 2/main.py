with open("input.txt") as f:
    input_lines = f.readlines()


def part1():
    valid_count = 0
    for line in input_lines:
        policy, password = line.split(":")
        min_n, max_n = policy.split("-")
        min_n = int(min_n)
        max_n = int(max_n.split(" ")[0])

        char = policy[-1]

        if max_n >= password.count(char) >= min_n:
            valid_count += 1
    print(valid_count)


def part2():
    valid_count = 0
    for line in input_lines:
        policy, password = line.split(":")
        pos_1, pos_2 = policy.split("-")
        pos_1 = int(pos_1)-1
        pos_2 = int(pos_2.split(" ")[0])-1

        password = password.strip()

        char = policy[-1]
        if bool(password[pos_1] == char) is not bool(password[pos_2] == char):
            valid_count += 1
    print(valid_count)


if __name__ == '__main__':
    part1()
    part2()
