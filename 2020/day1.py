import pprint

y, d = 2020, 1


def part1():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = [int(i) for i in f.read().splitlines() if int(i) < 2020]
    pprint.pprint(items)
    for item in items:
        print(f'item {type(item)}: {item}')
        for _item in items:
            print(f'_item {type(_item)}: {_item}')
            if item + _item == 2020:
                return item * _item

def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = [int(i) for i in f.read().splitlines() if int(i) < 2020]
    pprint.pprint(items)
    for item in items:
        print(f'item {type(item)}: {item}')
        for _item in items:
            print(f'_item {type(_item)}: {_item}')
            if item + _item >= 2020:
                continue
            for __item in items:
                if item + _item + __item == 2020:
                    return item * _item * __item


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
