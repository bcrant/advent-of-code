from collections import defaultdict
from pprint import pp


YEAR, DAY = 2018, 7


# [A]  <- [B]
#      <- [C]
# 
# {
#   "A": {
#
# }
#

class Node:
    def __init__(self, data):
        self.data = data
        self.curr = data[36] or None
        self.next = None
        self.prev = data[5] or None

    def __str__(self):
        return f"curr={self.curr} next={self.next} prev={self.prev} | data={self.data}"


def part1(items):
    nodes = defaultdict(dict)
    for item in items:
        node = Node(item)
        # print(f'node: {node}')
        if node.prev:
            nodes[node.prev][node.curr] = {}

    _nodes = {}
    for s in sorted(nodes.keys()):
        _nodes[s] = nodes[s]
    pp(_nodes)
    nodes = _nodes

    for prev_k, prev_v in nodes.items():
        curr_k = sorted(prev_v.keys())[0]
        if nodes.get(curr_k):
            nodes[prev_k][curr_k] = nodes[curr_k]
    
    pp(nodes)
    # ans = {}
    # for k, _v in nodes.items():
    #     # for _k, v in nodes.items():
    #         # if k not in v and k != _k:
    #     # if not nodes.get(v):
    #         # print(f"end of the road: {v}")
    #     ans[k] = {v: nodes.get(v)}
    # pp(ans)


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
