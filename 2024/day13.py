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
    # test base case with first machine.
    item = items[0]
    # expected: A button 80 times, B button 40 times == 280 tokens
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
    print(f'ax_maps {type(ax_maps)}: {ax_maps}')
    pp(ax_maps)
    print()

    print(f'bx_maps {type(bx_maps)}: {bx_maps}')
    pp(bx_maps)
    print()

    # Prize X position is evenly divisible by A or B button alone.
    print("Checking for evenly divisible...")
    if px in ax_maps.keys() or px in bx_maps.keys():
        match = ax_maps[px] or bx_maps[px]
        print(f"Exact match! x = {match}")

    # Brute force combinations of A and B button presses
    print("Checking for combinations...")
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

    pp(x_tokens)
    return min(x_tokens.keys())

    # y_maps = {}
    # for n in range(0, ayy):
    #     eq_str = f"n{n} * ay{ay} = {n*ay}"
    #     y_maps[eq_str] = (n, ay, n*ay)
    # print(f'y_maps {type(y_maps)}')
    # pp(y_maps)

    # while n <= axx:
    #     print(f"n*x {n * ax}")
    #     if n * ax == px:
    #         print(f"Match! n{n} * ax{ax} == px{px}")
    #     n += 1
    # return


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
