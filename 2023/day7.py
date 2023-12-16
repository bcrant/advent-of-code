from collections import defaultdict, deque
from pprint import pprint


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
        # print(f"hand: {hand}")
        # print(f"nums: {self.hand_numeric}")
        # print(f"bid : {bid}")
        self.uniq = set(self.hand)
        self.uniq_cnt = len(self.uniq)
        self.rank = self.set_rank()
        # print(f"rank: {self.rank}")

    def set_rank(self) -> int:
        if self.is_five_kind():
            return 6
        elif self.is_four_kind():
            return 5
        elif self.is_full_house():
            return 4
        elif self.is_three_kind():
            return 3
        elif self.is_two_pair():
            return 2
        elif self.is_one_pair():
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
    with open(f"{year}/data/day{day}_input_test.txt", "r") as f:
        items = [
            (item.split()[0], int(item.split()[1])) for item in f.read().splitlines()
        ]

    ranked = defaultdict(list[Hand])
    for hand, bid in items:
        h = Hand(hand, bid)
        ranked[h.rank].append(h)
    # pprint(ranked)

    # sorted_ranks = {}
    sorted_ranks = []
    for rank, hands in list(sorted(ranked.items())):
        # print(f'rank  {type(rank)}: {rank}')
        # print(f'hands {type(hands)}: {hands}')
        # sorted_ranks[rank] = {}
        # sorted_ranks[rank]["1before"] = [i.hand_numeric for i in hands]
        # sorted_ranks[rank]["1before"] = [i.hand_numeric for i in hands]
        if len(hands) == 1:
            # sorted_ranks[rank]["2after"] = [hands[0].hand_numeric]
            sorted_ranks.append(hands[0])
            continue

        sort_rank = []
        for i in range(0, len(hands) - 1):
            h1, h2 = hands[i], hands[i + 1]
            print(f"h1: {h1.hand}")
            print(f"h2: {h2.hand}")
            already_sorted = False
            for j in range(0, 5):
                print(j, h1.hand_numeric[j], h2.hand_numeric[j])
                if h1.hand_numeric[j] == h2.hand_numeric[j]:
                    print("equivalent")
                    continue
                if h1.hand_numeric[j] < h2.hand_numeric[j]:
                    print("less than")
                    already_sorted = True
                    break
                print("greater than?")
            if already_sorted:
                sort_rank.extend((h1, h2))
            else:
                sort_rank.extend((h2, h1))
            i += 1
        # sorted_ranks[rank]["2after"] = [i.hand_numeric for i in sort_rank]
        sorted_ranks.extend(sort_rank)

    winnings = 0
    for idx, i in enumerate(sorted_ranks):
        # print(idx+1, i.rank, i.hand, i.hand_numeric)
        _rank = idx + 1
        winnings += _rank * i.bid
        print(i.rank, _rank, "\t", i.bid, "\t", winnings, "\t", i.hand, i.hand_numeric)
    return winnings


# (
#     + 765 * 1
#     + 220 * 2
#     + 28 * 3
#     + 684 * 4
#     + 483 * 5
# )


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
