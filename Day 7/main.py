with open("input.txt") as f:
    input_lines = f.readlines()

# Not the prettiest of solutions but it was easy to work with
gold = "shiny gold"


def contains_gold(bags_dict, bag):
    if bag is gold:
        return True
    if not bag or bag not in bags_dict.keys():
        return False
    if gold in [x for x, _ in bags_dict[bag]]:
        return True
    for b, n in bags_dict[bag]:
        if contains_gold(bags_dict, b):
            return True
    return False


bags = {}


def part1():
    global bags
    bags = {}
    count = 0
    lines = [str(li.strip()[:-1]) for li in input_lines]
    for line in lines:
        c = " ".join(line.split()[:2]).strip()
        contains = " ".join(line.split()[4:])
        if contains != "no other bags":
            contains = [x.strip() for x in " ".join(line.split()[4:]).split(",")]
            if c not in bags.keys():
                bags[c] = []
            for x in contains:
                n = int(x[0])
                bag_name = " ".join(x.split()[1:3])
                bags[c].append([bag_name, n])
        else:
            bags[c] = []

    for bag, contains in bags.items():
        if contains_gold(bags, bag):
            count += 1

    return count


def count_bags(bag):
    if bag not in bags.keys() or not bags[bag][0][0]:
        return 1
    print([(b, n) for b, n in bags[bag]])
    return 1 + sum([n * count_bags(b) for b, n in bags[bag]])


def part2():
    global bags
    bags = {}
    lines = [str(li.strip()[:-1]) for li in input_lines]
    for line in lines:
        c = " ".join(line.split()[:2]).strip()
        contains = " ".join(line.split()[4:])
        if contains != "no other bags":
            contains = [x.strip() for x in " ".join(line.split()[4:]).split(",")]
            if c not in bags.keys():
                bags[c] = []
            for x in contains:
                n = int(x[0])
                bag_name = " ".join(x.split()[1:3])
                bags[c].append([bag_name, n])
        else:
            bags[c] = [[None, 1]]

    return count_bags(gold) - 1


if __name__ == "__main__":
    print(part1())
    print(part2())
