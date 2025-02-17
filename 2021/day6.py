from pprint import pp


YEAR, DAY = 2021, 6


def part1(items: list):
    days = {0: items}
    for days_n in range(1, 81):
        item = [n - 1 for n in days[days_n - 1]]
        for i, n in enumerate(item):
            if n == -1:
                item[i] = 6
                item.append(8)
        days[days_n] = item
    return len(days[80])


def part2(items):
    ans = 0
    current_states = {
        0: items.count(0),
        1: items.count(1),
        2: items.count(2),
        3: items.count(3),
        4: items.count(4),
        5: items.count(5),
        6: items.count(6),
        7: items.count(7),
        8: items.count(8),
    }

    next_states = {}
    for _ in range(256):
        next_states = {
            0: current_states[1],
            1: current_states[2],
            2: current_states[3],
            3: current_states[4],
            4: current_states[5],
            5: current_states[6],
            6: current_states[7],
            7: current_states[8],
            8: current_states[0],
        }

        # Reset adult fish at 0 to 6
        if current_states[0] > 0:
            next_states[6] += current_states[0]

        # Move value of new_states to current_states, reset value new_states
        current_states = next_states
        next_states = {}

    # After all days completed, sum up the values of all states
    for fish in current_states:
        ans += current_states[fish]
    return ans


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = list(map(int, f.read().split(",")))
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
