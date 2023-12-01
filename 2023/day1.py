# fmt: off
import re


year, day = 2023, 1


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()    
    
    items = [
        re.sub("[^0-9]", "", item)
        for item in f.read().splitlines()
    ]
    nums = [
        int("".join(item[0], item[-1]))
        for item in items
    ]    
    return sum(nums)


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    word_to_int = {
        # edge cases first
        "oneight": "18",
        "eightwo": "82",
        "eighthree": "83",
        "threeight": "38",
        "twone": "21",
        # words to int
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    _items = []
    for item in items:
        _item = item
        for k, v in word_to_int.items():
            _item = _item.replace(k, v)
        _item = re.sub("[^0-9]", "", _item)
        _items.append(_item)
    nums = [
        int("".join((item[0], item[-1]))) 
        for item in _items
    ]
    return sum(nums)


# fmt: on
if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
