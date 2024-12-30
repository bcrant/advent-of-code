"""
1. Initialize an incrementing ID for each region
2. Breadth first search starting at (0, 0)
3. TODO(brian) Will likely need to determine if a region is inside of another region
4. Calculate area and perimeter of each region
"""

from collections import defaultdict, deque
from pprint import pp
from typing import List, Tuple


YEAR, DAY = 2024, 12

MOVE_E = MOVE_EAST = (1, 0)
MOVE_N = MOVE_NORTH = (0, -1)
MOVE_S = MOVE_SOUTH = (0, 1)
MOVE_W = MOVE_WEST = (-1, 0)
MOVES = {
    "E": MOVE_E,
    "N": MOVE_N,
    "S": MOVE_S,
    "W": MOVE_W,
}


# def part1(items):
# w, h = len(items[0]), len(items)
# coords = []
# for x in range(0, h):
#     for y in range(0, w):
#         coords.append((x, y))
# pp(items)
# # pp(coords)

#     queue = deque(coords)
#     visited = set()

#     region_id = 0
#     regions = defaultdict(set)
#     while queue:

#         # Dequeue a vertex from the queue
#         x, y = node = queue.popleft()
#         plant = items[y][x]
#         print(f'position: {node}  plant: {plant}')

#         if node not in visited:
#             # Mark the node as visited and process it
#             visited.add(node)

#         # # Base case: Visisted all nodes
#         # if len(visited) == len(coords):
#         #     break

#         # Enqueue all adjacent unvisited nodes
#         neighbors = get_valid_adjacentmvs(items, node)
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 regions[region_id].add((node))

#         region_id += 1

#     print()
#     print("Regions...")
#     pp(dict(regions))
#     print()

#     return


def part1(grid: List[str]) -> int:
    """I used chatgpt for this because it is December 29th and christmas is ruined!"""

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    total_cost = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant = grid[r][c]
                queue = deque()
                queue.append((r, c))
                visited[r][c] = True
                area = 0
                perimeter = 0

                while queue:
                    curr_r, curr_c = queue.popleft()
                    area += 1

                    for dr, dc in MOVES.values():
                        nr, nc = curr_r + dr, curr_c + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            perimeter += 1
                        elif grid[nr][nc] != plant:
                            perimeter += 1
                        else:
                            if not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))

                region_cost = area * perimeter
                total_cost += region_cost

    return total_cost


def part2(grid: List[str]) -> int:
    """Modified this on my own, but unsuccessful in counting the corners in each garden."""

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    region_id = 0
    regions = defaultdict(dict)
    total_cost = 0
    for y in range(rows):
        for x in range(cols):
            if not visited[y][x]:
                plant = grid[y][x]

                queue = deque()
                queue.append((x, y))
                visited[y][x] = True
                area = 0
                corners = 0
                perimeter = 0
                neighbors = 0
                region = []

                while queue:
                    cx, cy = queue.popleft()
                    region.append((cx, cy))
                    area += 1

                    for dx, dy in MOVES.values():
                        nx, ny = cx + dx, cy + dy

                        if nx >= 0 and nx < rows and ny >= 0 and ny < cols:
                            if grid[ny][nx] != plant:
                                neighbors += 1

                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                            perimeter += 1
                        elif grid[ny][nx] != plant:
                            perimeter += 1
                        else:
                            if not visited[ny][nx]:
                                visited[ny][nx] = True
                                queue.append((nx, ny))

                        if neighbors >= 2:
                            corners += 1

                meta = {
                    "area": area,
                    "corners": corners,
                    "neighbors": neighbors,
                    "perimeter": perimeter,
                    "region": region,
                }
                regions[f"{plant}{region_id}"] = meta
                region_id += 1
                region_cost = area * perimeter
                total_cost += region_cost

    for region_id, v in regions.items():
        print()
        pretty = {k: _v for k, _v in v.items() if k != "region"}
        pp(pretty)
        print(region)
        visualize_region(items, v)

    return total_cost


def visualize_region(items, values: list) -> None:
    w, h = len(items[0]), len(items)
    coords = [["⬛" for _ in range(w)] for _ in range(h)]
    points = values["region"]
    for point in points:
        x, y = point
        coords[y][x] = "🟩"
    for line in coords:
        print("".join(line))


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


def tapout_part2(items):
    """I'm once again using Jonathan Paulson's answer to keep moving..."""
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left
    p1 = 0
    p2 = 0
    D = items

    G = D
    R = len(G)
    C = len(G[0])

    SEEN = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in SEEN:
                continue
            Q = deque([(r, c)])
            area = 0
            perim = 0
            PERIM = dict()
            while Q:
                r2, c2 = Q.popleft()
                if (r2, c2) in SEEN:
                    continue
                SEEN.add((r2, c2))
                area += 1
                for dr, dc in DIRS:
                    rr = r2 + dr
                    cc = c2 + dc
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r2][c2]:
                        Q.append((rr, cc))
                    else:
                        perim += 1
                        if (dr, dc) not in PERIM:
                            PERIM[(dr, dc)] = set()
                        # side = same direction, adjacent
                        PERIM[(dr, dc)].add((r2, c2))

            sides = 0
            for k, vs in PERIM.items():
                SEEN_PERIM = set()
                old_sides = sides
                for pr, pc in vs:
                    if (pr, pc) not in SEEN_PERIM:
                        sides += 1
                        Q = deque([(pr, pc)])
                        while Q:
                            r2, c2 = Q.popleft()
                            if (r2, c2) in SEEN_PERIM:
                                continue
                            SEEN_PERIM.add((r2, c2))
                            for dr, dc in DIRS:
                                rr, cc = r2 + dr, c2 + dc
                                if (rr, cc) in vs:
                                    Q.append((rr, cc))

            p1 += area * perim
            p2 += area * sides

    return p2


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"test1 answer: 1930")
    # print(f"part2 answer: {part2(items)}")
    # print(f"test2 answer: 1206")
    print(f"part2 answer: {tapout_part2(items)}")
