from collections import defaultdict


year, day = 2023, 4


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [
            [i.strip().split() for i in item.split(":")[1].split("|")]
            for item in f.read().splitlines()
        ]

    points = 0
    cards = defaultdict(int)
    for game, card in enumerate(items):
        cards[game] += 1
        winners = [int(n) for n in card[0]]
        picks = [int(n) for n in card[1]]
        cnt = len(set(winners) & set(picks))
        if cnt > 0:
            points += 2 ** (cnt - 1)
        for i in range(cnt):
            cards[game + 1 + i] += cards[game]
    return points


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [
            [i.strip().split() for i in item.split(":")[1].split("|")]
            for item in f.read().splitlines()
        ]

    points = 0
    cards = defaultdict(int)
    for game, card in enumerate(items):
        cards[game] += 1
        winners = [int(n) for n in card[0]]
        picks = [int(n) for n in card[1]]
        cnt = len(set(winners) & set(picks))
        if cnt > 0:
            points += 2 ** (cnt - 1)
        for i in range(cnt):
            cards[game + 1 + i] += cards[game]
    return sum(cards.values())


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
