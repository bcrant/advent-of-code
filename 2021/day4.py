y, d = 2021, 4


def part1():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        # with open(f"{y}/data/day{d}_example.txt", "r") as f:
        items = f.read().splitlines()

    picks = [int(i) for i in items[0].split(",")]
    print(f"picks {type(picks)} {picks}")

    # Remove picks and first separator
    items = items[2:]

    cards = []
    card = []
    for idx, item in enumerate(items):
        row = list(map(int, item.split()))
        if item == "":
            cards.append(card)
            card = []
        elif idx == len(items) - 1:
            card.append(row)
            cards.append(card)
            card = []
        else:
            card.append(row)
    del card

    winning_card = winning_nums = nums = []
    drawn = 0
    bingo = False
    while not bingo:
        nums = picks[0:drawn]
        for card_idx, card in enumerate(cards):
            for row_idx, row in enumerate(card):
                if all(n in nums for n in row):
                    winning_card, winning_nums = card, nums
                    bingo = True
            cols = [*list(zip(*card))]
            for col_idx, col in enumerate(cols):
                if all(n in nums for n in col):
                    winning_card, winning_nums = cols, nums
                    bingo = True
        drawn += 1
    flattened_card = [
        item for sublist in winning_card for item in sublist if item not in winning_nums
    ]
    return sum(flattened_card) * nums[-1]


def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        # with open(f"{y}/data/day{d}_example.txt", "r") as f:
        items = f.read().splitlines()

    picks = [int(i) for i in items[0].split(",")]
    print(f"picks {type(picks)} {picks}")

    # Remove picks and first separator
    items = items[2:]

    cards = []
    card = []
    for idx, item in enumerate(items):
        row = list(map(int, item.split()))
        if item == "":
            cards.append(card)
            card = []
        elif idx == len(items) - 1:
            card.append(row)
            cards.append(card)
            card = []
        else:
            card.append(row)
    del card

    bingo = {i: False for i in range(len(cards))}
    winning_card = winning_nums = nums = []
    drawn = 0
    while not all(i is True for i in bingo.values()):
        nums = picks[0:drawn]
        for card_idx, card in enumerate(cards):
            for row_idx, row in enumerate(card):
                if all(n in nums for n in row):
                    if not bingo[card_idx]:
                        winning_card, winning_nums = card, nums
                        bingo[card_idx] = True
            cols = [*list(zip(*card))]
            for col_idx, col in enumerate(cols):
                if all(n in nums for n in col):
                    if not bingo[card_idx]:
                        winning_card, winning_nums = cols, nums
                        bingo[card_idx] = True
        drawn += 1
    flattened_card = [
        item for sublist in winning_card for item in sublist if item not in winning_nums
    ]
    return sum(flattened_card) * nums[-1]


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
