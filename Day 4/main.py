with open("input.txt") as f:
    input_lines = f.readlines()


def part1():
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    strings = [x[:-1] for x in input_lines]
    fields = []
    valid_count = 0

    for s in strings:
        if not s:
            if all([r in fields for r in required]):
                valid_count += 1
            fields = []
        fields.extend([x.split(":")[0] for x in s.split(" ")])

    return valid_count


def part2():  # Om ändå jag kunde regex
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_c = "0123456789abcdef"
    strings = [x[:-1] for x in input_lines]
    fields = {}
    valid_count = 0

    for s in strings:
        if not s:
            if all([r in fields.keys() for r in required]):
                try:
                    valid_hgt = ("cm" == fields["hgt"][-2:] and 150 <= int(fields["hgt"][:-2]) <= 193) or ("in" == fields["hgt"][-2:] and 59 <= int(fields["hgt"][:-2]) <= 76)
                    valid_hcl = "#" == fields["hcl"][0] and len(fields["hcl"]) == 7 and all(c in valid_c for c in fields["hcl"][1:])
                    valid_ecl = fields["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    valid_pid = len(fields["pid"]) == 9 and int(fields["pid"])

                    if 2002 >= int(fields["byr"]) >= 1920 and \
                       2020 >= int(fields["iyr"]) >= 2010 and \
                       2030 >= int(fields["eyr"]) >= 2020 and \
                       valid_hgt and valid_hcl and valid_ecl and valid_pid:
                        print(fields)
                        valid_count += 1

                except Exception as e:
                    print(e, "======\n", fields)
            fields = {}
        for k, v in [(x.split(":")[0], x.split(":")[1]) if x else (None, None) for x in s.split(" ")]:
            if k and v:
                fields[k] = v
    return valid_count


if __name__ == "__main__":
    print(part1())
    print(part2())