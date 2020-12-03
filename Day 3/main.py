with open("input.txt") as f:
    input_lines = f.readlines()


def part1(delta_x, delta_y):
    m = [list(x[:-1]) for x in input_lines]
    trees = 0
    m_len = len(m[0])
    x, y = 0, 0
    try:
        while True:
            trees += int(m[y][x] == "#")
            m[y][x] = "X" if m[y][x] == "#" else "O"
            # print(m[y])
            y += delta_y
            x += delta_x
            x = x % m_len
    except IndexError:
        return trees


def part2():
    print(part1(1, 1)*part1(3, 1)*part1(5, 1)*part1(7, 1)*part1(1, 2))


if __name__ == "__main__":
    print(part1(3, 1))
    part2()