from pprint import pprint


year, day = 2020, 4


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    # pprint(items)

    passports = []
    tmp = []
    for item in items:
        if item:
            tmp.extend([i.split(":") for i in item.split(" ")])
        elif item == "":
            passport = {k: v for k, v in tmp if k != "cid"}
            passports.append(passport)
            tmp = []

    VALID_KEYS = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    cnt = 0
    for pp in passports:
        _keys = set((pp.keys()))
        if _keys == VALID_KEYS:
            cnt += 1
    return cnt


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    # pprint(items)

    passports = []
    tmp = []
    for item in items:
        if item:
            tmp.extend([i.split(":") for i in item.split(" ")])
        elif item == "":
            passport = {k: v for k, v in tmp if k != "cid"}
            passports.append(passport)
            tmp = []

    VALID_KEYS = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    cnt = 0
    valid_pp = []
    for pp in passports:
        _keys = set((pp.keys()))
        valid = True
        if _keys != VALID_KEYS:
            continue

        if not all(len(pp[e]) == 4 for e in ("byr", "iyr", "eyr")):
            print("a", pp)
            valid = False

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not (int(pp["byr"]) >= 1920 and int(pp["byr"]) <= 2002):
            print("b", pp)
            valid = False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not (int(pp["iyr"]) >= 2010 and int(pp["iyr"]) <= 2020):
            print("c ", pp["iyr"])
            valid = False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not (int(pp["eyr"]) >= 2020 and int(pp["eyr"]) <= 2030):
            print("d ", pp["eyr"])
            valid = False

        # hgt (Height) - a number followed by either cm or in:
        if not str(pp["hgt"][0]).isnumeric():
            print("e1", pp["hgt"])
            valid = False
        elif str(pp["hgt"]).endswith("cm"):
            cm = int(str(pp["hgt"]).removesuffix("cm"))
            if not (cm >= 150 and cm <= 193):
                print("e2", pp["hgt"])
                valid = False
        elif str(pp["hgt"]).endswith("in"):
            _in = int(str(pp["hgt"]).removesuffix("in"))
            if not (_in >= 59 and _in <= 76):
                print("e3", pp["hgt"])
                valid = False
        else:
            valid = False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not str(pp["hcl"]).startswith("#"):
            print("f1", pp["hcl"])
            valid = False
        if not len(pp["hcl"][1:]) == 6:
            print("f2", pp["hcl"])
            valid = False
        valid_colors = [*range(0, 10), "a", "b", "c", "d", "e", "f"]
        valid_colors = [str(i) for i in valid_colors]
        if not (e in valid_colors for e in pp["hcl"][1:]):
            print("f3", pp["hcl"])
            valid = False

        # ecl (Eye Color) - exactly one of: "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
        if not pp["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            print("g ", pp["ecl"])
            valid = False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not (len(pp["pid"]) == 9 and str(pp["pid"]).isnumeric()):
            print("h ", pp["pid"], len(pp["pid"]), str(pp["pid"]).isnumeric())
            valid = False

        if valid:
            cnt += 1
            valid_pp.append(pp)
    print(f"cnt {type(cnt)}: {cnt}")
    pprint(valid_pp)
    return cnt


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
