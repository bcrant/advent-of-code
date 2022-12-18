""" https://adventofcode.com/2022/day/8 """


def part1():
    # with open("./data/day8_example.txt", "r") as f:
    with open("./data/day8_input.txt", "r") as f:
        grid = [list(map(int, line)) for line in f.read().splitlines()]

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            curr = grid[row][col]
            if (
                all(grid[row][x] < curr for x in range(col))
                or all(grid[row][x] < curr for x in range(col + 1, len(grid[row])))
                or all(grid[x][col] < curr for x in range(row))
                or all(grid[x][col] < curr for x in range(row + 1, len(grid)))
            ):
                total += 1
    return total


def part2():
    # with open("./data/day8_example.txt", "r") as f:
    with open("./data/day8_input.txt", "r") as f:
        grid = [list(map(int, line)) for line in f.read().splitlines()]

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            curr = grid[row][col]
            left = right = up = down = 0
            for x in range(col - 1, -1, -1):
                left += 1
                if grid[row][x] >= curr:
                    break
            for x in range(col + 1, len(grid[row])):
                right += 1
                if grid[row][x] >= curr:
                    break
            for x in range(row - 1, -1, -1):
                up += 1
                if grid[x][col] >= curr:
                    break
            for x in range(row + 1, len(grid)):
                down += 1
                if grid[x][col] >= curr:
                    break
            total = max(total, up * down * left * right)
    return total


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
