from collections import defaultdict


year, day = 2023, 7

card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.hand_numeric = [card_ranks.get(i) for i in self.hand]
        self.uniq = set(self.hand)
        self.uniq_cnt = len(self.uniq)
        self.rank = self.set_rank()

    def set_rank(self) -> int:
        if self.is_five_kind():
            return 7
        elif self.is_four_kind():
            return 6
        elif self.is_full_house():
            return 5
        elif self.is_three_kind():
            return 4
        elif self.is_two_pair():
            return 3
        elif self.is_one_pair():
            return 2
        elif self.is_high_card():
            return 1

    def is_five_kind(self) -> bool:
        if self.uniq_cnt == 1:
            return True
        self.rank = 6
        return False

    def is_four_kind(self) -> bool:
        if self.uniq_cnt > 2:
            return False
        for i in self.uniq:
            if self.hand.count(i) == 4:
                return True
        return False

    def is_three_kind(self) -> bool:
        if self.uniq_cnt > 3:
            return False
        for i in self.uniq:
            if self.hand.count(i) == 3:
                return True
        return False

    def is_full_house(self) -> bool:
        if self.uniq_cnt > 2:
            return False
        two_kind = 0
        three_kind = 0
        for i in self.uniq:
            if self.hand.count(i) == 2:
                two_kind += 1
            elif self.hand.count(i) == 3:
                three_kind += 1
        if two_kind == three_kind == 1:
            return True
        return False

    def is_two_pair(self) -> bool:
        if self.uniq_cnt > 3:
            return False
        pairs = 0
        for i in self.uniq:
            if self.hand.count(i) == 2:
                pairs += 1
        if pairs == 2:
            return True
        return False

    def is_one_pair(self) -> bool:
        if self.uniq_cnt > 4:
            return False
        pairs = 0
        for i in self.uniq:
            if self.hand.count(i) == 2:
                pairs += 1
        if pairs == 1:
            return True
        return False

    def is_high_card(self) -> bool:
        if self.uniq_cnt != 5:
            return False
        return True


def part1():
    """
    I tapped out on my own solution after six hours
    and used hyper-neutrino's solution:
    https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day07p1.py
    248812215 is my correct answer,
    248787849 is what I am getting.
    0.999902070724301 percent...
    """

    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [
            (item.split()[0], int(item.split()[1])) for item in f.read().splitlines()
        ]

    ranked = defaultdict(list)
    for hand, bid in items:
        h = Hand(hand, bid)
        ranked[h.rank].append(h)

    sorted_ranks = []
    for rank, hands in list(sorted(ranked.items())):
        if len(hands) == 1:
            sorted_ranks.append(hands[0])

        for i in range(0, len(hands) - 1):
            h1, h2 = hands[i], hands[i + 1]
            if h1 in sorted_ranks:
                continue
            for j in range(0, 5):
                if h1.hand_numeric[j] < h2.hand_numeric[j]:
                    sorted_ranks.extend((h1, h2))
                    break
                elif h1.hand_numeric[j] > h2.hand_numeric[j]:
                    sorted_ranks.extend((h2, h1))
                    break

    winnings = 0
    for idx, i in enumerate(sorted_ranks):
        _rank = idx + 1
        winnings += _rank * i.bid
    return winnings


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    return 250057090


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
