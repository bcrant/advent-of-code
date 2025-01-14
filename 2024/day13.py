import math
import re
from collections import namedtuple
from itertools import product
from pprint import pp


YEAR, DAY = 2024, 13
TOKENS_A = 3
TOKENS_B = 1

ClawMachine = namedtuple("ClawMachine", ["a", "b", "p"])

# The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.


def part1(items):
    result = {}
    for item in items:
        print(f'item {type(item)}: {item}')
        result[str(item)] = route_machine(item)
    pp(result)
    return result


def route_machine(item):
    print(item)

    ax, ay = item.a
    bx, by = item.b
    px, py = item.p

    # Solve for...
    # (ax * k) + (bx * j) = px
    # (ay * m) + (by * n) = py

    axx = math.ceil(px / ax)
    ayy = math.ceil(py / ay)
    bxx = math.ceil(px / bx)
    byy = math.ceil(py / by)
    print(f"axx = px{px} / ax{ax} = {axx}")
    print(f"bxx = px{px} / bx{ax} = {bxx}")
    print(f"ayy = py{py} / ay{ay} = {ayy}")
    print(f"byy = py{py} / by{ay} = {byy}")


    ax_maps = {
        n*ax: n
        for n in range(0, axx)
    }    
    bx_maps = {
        n*bx: n
        for n in range(0, bxx)
    }
    ay_maps = {
        n*ay: n
        for n in range(0, ayy)
    }    
    by_maps = {
        n*by: n
        for n in range(0, byy)
    }


    # Prize X position is evenly divisible by A or B button alone.
    if px in ax_maps.keys() or px in bx_maps.keys():
        match = ax_maps[px] or bx_maps[px]
        print(f"Exact match! x = {match}")

    # Brute force combinations of A and B button presses
    x_tokens = {}
    for ax in ax_maps.keys():
        for bx in bx_maps.keys():
            cx = ax + bx
            if cx == px:
                ab = ax_maps[ax]
                bb = bx_maps[bx]
                total_tokens = (ab * TOKENS_A) + (bb * TOKENS_B)
                # print(f"Combined match! ax+bx=cx {ax}+{bx}={cx} --> Button presses: (A={ab}, B={bb}) --> {total_tokens} tokens")
                x_tokens[total_tokens] = (ab, bb)
                break

    print(f'x_tokens {type(x_tokens)}:')
    pp(x_tokens)
    min_x_tokens = min(x_tokens.keys()) if x_tokens.keys() else None
    print(f'min_x_tokens: {min_x_tokens}')

    y_tokens = {}
    for ay in ay_maps.keys():
        for by in by_maps.keys():
            cy = ay + by
            if cy == py:
                ab = ay_maps[ay]
                bb = by_maps[by]
                total_tokens = (ab * TOKENS_A) + (bb * TOKENS_B)
                # print(f"Combined match! ay+by=cy {ay}+{by}={cy} --> Button presses: (A={ab}, B={bb}) --> {total_tokens} tokens")
                y_tokens[total_tokens] = (ab, bb)
                break

    print(f'y_tokens {type(y_tokens)}')
    pp(y_tokens)
    min_y_tokens = min(y_tokens.keys()) if y_tokens.keys() else None
    print(f'min_y_tokens: {min_y_tokens}')

    ans = min([k for k in x_tokens.keys() if k in y_tokens.keys()])
    return ans


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
    print(f"test1 answer: 480")
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
