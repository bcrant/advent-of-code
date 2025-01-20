import math
import re
from collections import namedtuple
from pprint import pp


YEAR, DAY = 2024, 13
TOKENS_A = 3
TOKENS_B = 1
MAX_BUTTON_PRESSES = 100

ClawMachine = namedtuple("ClawMachine", ["a", "b", "p"])


def part1(items):
    tokens = 0
    for item in items:
        print(item)
        tokens += route_machine(item) or 0
    return tokens


def route_machine(item):
    """Solve for...
    (ax * k) + (bx * j) = px
    (ay * m) + (by * n) = py
    """
    ax, ay = item.a
    bx, by = item.b
    px, py = item.p

    axx = math.ceil(px / ax)
    ayy = math.ceil(py / ay)
    bxx = math.ceil(px / bx)
    byy = math.ceil(py / by)
    print(f"axx = px{px} / ax{ax} = {axx}")
    print(f"bxx = px{px} / bx{bx} = {bxx}")
    print(f"ayy = py{py} / ay{ay} = {ayy}")
    print(f"byy = py{py} / by{by} = {byy}")

    ax_maps = {n * ax: n for n in range(0, axx + 1)}
    bx_maps = {n * bx: n for n in range(0, bxx + 1)}
    ay_maps = {n * ay: n for n in range(0, ayy + 1)}
    by_maps = {n * by: n for n in range(0, byy + 1)}

    # Brute force combinations of A and B button presses
    x_tokens = {}
    for ax in ax_maps.keys():
        for bx in bx_maps.keys():
            cx = ax + bx
            if cx != px:
                continue
            ab = ax_maps[ax]
            bb = bx_maps[bx]
            if ab > MAX_BUTTON_PRESSES or bb > MAX_BUTTON_PRESSES:
                break
            cnt = (ab * TOKENS_A) + (bb * TOKENS_B)
            x_tokens[cnt] = (ab, bb)

    y_tokens = {}
    for ay in ay_maps.keys():
        for by in by_maps.keys():
            cy = ay + by
            if cy != py:
                continue
            ab = ay_maps[ay]
            bb = by_maps[by]
            if ab > MAX_BUTTON_PRESSES or bb > MAX_BUTTON_PRESSES:
                break
            cnt = (ab * TOKENS_A) + (bb * TOKENS_B)
            y_tokens[cnt] = (ab, bb)

    ans = 0
    if not x_tokens.keys() and not y_tokens.keys():
        return ans

    matches = [k for k in x_tokens.keys() if k in y_tokens.keys()]
    if matches:
        ans = min(matches)
        if len(matches) > 1:
            print(f"matches: {matches} -> min(matches): {ans}")
    return ans


def part2():
    """
    Tapped out for parts 1 and 2. Part 1 I was off by 55. There is an edge case
    I am unsure of where I found two possible matches [262, 317] and select the
    minimum of these two, which is 55 short of the correct answer -- which I yet
    again borrowed from Jonathan Paulson.
    """
    import z3

    def ints(s):
        return [int(x) for x in re.findall("\d+", s)]

    with open(f"{YEAR}/data/day{DAY}_input.txt", "r") as f:
        D = f.read().strip()

    p1 = 0
    p2 = 0

    def solve(ax, ay, bx, by, px, py, part2):
        P2 = 10000000000000 if part2 else 0
        px += P2
        py += P2

        t1 = z3.Int("t1")
        t2 = z3.Int("t2")
        SOLVE = z3.Solver()
        SOLVE.add(t1 > 0)
        SOLVE.add(t2 > 0)
        SOLVE.add(t1 * ax + t2 * bx == px)
        SOLVE.add(t1 * ay + t2 * by == py)
        if SOLVE.check() == z3.sat:
            M = SOLVE.model()
            ret = M.eval(3 * t1 + t2).as_long()
            return ret
        else:
            return 0

    machines = D.split("\n\n")
    for i, machine in enumerate(machines):
        ax, ay, bx, by, px, py = ints(machine)
        p1 += solve(ax, ay, bx, by, px, py, False)
        p2 += solve(ax, ay, bx, by, px, py, True)

    return p2


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
    print(f"part2 answer: {part2()}")
