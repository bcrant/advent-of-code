import re
from collections import namedtuple
from pprint import pp


YEAR, DAY = 2024, 13

ClawMachine = namedtuple("ClawMachine", ["a", "b", "p"])


def part1(items):
    pp(items)
    for item in items:
        print()
        print(item)

        ax, ay = item.a
        bx, by = item.b
        px, py = item.p

        # Solve for...
        # (ax * k) + (bx * j) = px
        # (ay * m) + (by * n) = py

        n = 0
        c = 0
        axx = px / ax
        ayy = py / ay
        print(f"px{px} / ax{ax} = {axx}")
        while n < axx:
            n += 1

        yy = py / ay
        print(f"py{py} / ax{ay} = {yy}")
    return


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().split("\n\n")
    claw_machines = []
    for item in items:
        ax, ay = item.split(": ")[1].split("\n")[0].split(", ")
        a = [strip_non_digits(ax), strip_non_digits(ay)]
        bx, by = item.split(": ")[2].split("\n")[0].split(", ")
        b = [strip_non_digits(bx), strip_non_digits(by)]
        px, py = item.split(": ")[3].split("\n")[0].split(", ")
        p = [strip_non_digits(px), strip_non_digits(py)]
        claw_machines.append(ClawMachine(a, b, p))
    return claw_machines


def strip_non_digits(s: str) -> int:
    return int(re.sub(r"\D", "", s))


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
