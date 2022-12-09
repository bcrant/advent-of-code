""" https://adventofcode.com/2022/day/7 """

from collections import defaultdict, deque


def part1():
    # Parse input
    with open("./data/day7_input.txt", "r") as f:
        items = [
            line
            for line in f.read().splitlines()
            if line != "$ ls" and line != "$ cd .."
        ]

    # Group contents
    curr_dir = ""
    dir_contents = defaultdict(list)
    parent_nodes = defaultdict(list)
    child_parent = {}
    for item in items:
        if "$ cd " in item:
            curr_dir = item.replace("$ cd ", "")
        else:
            meta, name = item.split(' ')
            dir_contents[curr_dir].append((meta, name))
            if meta == "dir":
                child_parent[name] = curr_dir
                parent_nodes[curr_dir].append(name)

    # Find innermost nodes (dirs that do not contain dirs)
    innermost_dirs = {}
    for parent, children in dir_contents.items():
        metas = [child[0] for child in children]
        if "dir" not in metas:
            size = sum(map(int, metas))
            innermost_dirs[parent] = size

    inner_dirs = [deque([i]) for i in innermost_dirs.keys()]
    tree_paths = [deque(['/'])]
    for child in inner_dirs:
        parent_node = child_parent.get(child[0])
        while parent_node is not None:
            child.appendleft(parent_node)
            parent_node = child_parent.get(parent_node)
        tree_paths.append(child)

    dir_sizes = {
        k: {'size': v, 'dirs': []}
        for k, v in innermost_dirs.items()
    }

    for dir_name, dir_content in dir_contents.items():
        sizes = [n[0] for n in dir_content if n[0] != "dir"]
        dir_names = [n[1] for n in dir_content if n[0] == "dir"]
        dir_sizes[dir_name] = {
            'size': sum(map(int, sizes)),
            'dirs': dir_names
        }

    remaining = check_remaining(dir_sizes)
    while remaining:
        dir_sizes = add_dir_size(dir_sizes)
        remaining = check_remaining(dir_sizes)

    answer1 = sum([v["size"] for v in dir_sizes.values() if v["size"] <= 100000])
    return answer1

def add_dir_size(dir_sizes_dict: dict):
    for log in dir_sizes_dict.values():
        if log["dirs"]:
            for d in log["dirs"]:
                s = dir_sizes_dict.get(d).get('size')
                log["size"] += dir_sizes_dict.get(d).get('size')
                log["dirs"].remove(d)
    return dir_sizes_dict


def check_remaining(dir_sizes_dict: dict) -> bool:
    if any(bool(log["dirs"]) for log in dir_sizes_dict.values()):
        return True




    #     if s == 0:
    #         dirs = [n[1] for n in dir_contents.get(d) if n[0] != "dir"]
    #         dir_sizes[d] = dir_contents.get(d)
    # print('\n\n dir sizes after')
    # pprint.pprint(dir_sizes)

    # dsizes = {}
    # for tree_path in tree_paths:
    #     for node in tree_path:
    #         dsizes[node] += dir_contents
    #     print(f"tree_path: {tree_path}")

    # while True:
    #     for inner_dir, size in innermost_dirs.items():
    #         parent = child_parent.get(inner_dir)
    #         if parent:
    #             dir_sizes[parent] += size
    # # pprint.pprint(dir_sizes)
    # print(len(dir_sizes))


    # tree = defaultdict(list)
    # depth = 0
    # tree[depth] = ['/']
    # nodes = []
    # for child, parent in child_parent.items():
    #     node = deque([parent, child])
    #     print(node)
    #     if parent != "/":
    #         node.appendleft(child_parent[parent])  # grandparent
    #     node.append(child_parent[child])   # grandchild
    #     nodes.append(node)
    # pprint.pprint(nodes)

    # Measure file sizes
    # dir_sizes = {}
    # for dir_name, children in dir_contents.items():
    #     file_size = 0
    #     for child in children:
    #         if child[0] != "dir":
    #             file_size += int(child[0])
    #     dir_sizes[dir_name] = file_size

    # part1_sum = 0
    # for dname, dsize in dir_sizes.items():
    #     print(dname, dsize)
    #     if dsize <= 100000:
    #         part1_sum += dsize
    # print('ANSWER: ', part1_sum)
    # return


def part2():
    with open("./data/day7_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    # print(f"part2 answer: {part2()}")
