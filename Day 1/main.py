with open("nums.txt") as f:
    lines = [int(x) for x in f.readlines()]


def part1():
    for x in lines:
        for y in lines:
            if x+y == 2020:
                print(x, " + ", y, " = ", x*y)
                return


def part2():
    for x in lines:
        for y in lines:
            for z in lines:
                if x + y + z == 2020:
                    print(x, " + ", y, " + ", z, " = ", x * y * z)
                    return


if __name__ == '__main__':
    part1()
    part2()