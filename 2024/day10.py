from collections import defaultdict, deque
from pprint import pp
from typing import List, Tuple


YEAR, DAY = 2024, 10

START = "0"
END = "9"

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


def part1(items):
    # pp(items)
    start_positions: List[int, int] = []
    end_positions: List[int, int] = []
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            if val == START:
                start_positions.append((x, y))
            elif val == END:
                end_positions.append((x, y))

    trails = defaultdict(int)
    for start_pos in start_positions:
        queue = deque([start_pos])
        visited = set()
        reachable = set()

        while queue:
            # Dequeue a vertex from the queue
            current_node = queue.popleft()

            if current_node not in visited:
                # Mark the node as visited and process it
                visited.add(current_node)

            # Base case: Reached target
            if current_node in end_positions:
                reachable.add((start_pos, current_node))

            # Enqueue all adjacent unvisited nodes
            neighbors = get_valid_adjacent_moves(items, current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        trails[start_pos] += len(reachable)

    ans = sum(trails.values())
    return ans


def part2(items):
    # pp(items)
    start_positions: List[int, int] = []
    end_positions: List[int, int] = []
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            if val == START:
                start_positions.append((x, y))
            elif val == END:
                end_positions.append((x, y))

    trails = defaultdict(int)
    for start_pos in start_positions:
        queue = deque([start_pos])
        visited = set()
        reachable = list()

        while queue:
            # Dequeue a vertex from the queue
            current_node = queue.popleft()
            # print(f'current_node: {current_node}')

            if current_node not in visited:
                # Mark the node as visited and process it
                visited.add(current_node)

            # Base case: Reached target
            if current_node in end_positions:
                reachable.append((start_pos, current_node))

            # Enqueue all adjacent unvisited nodes
            neighbors = get_valid_adjacent_moves(items, current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        trails[start_pos] += len(reachable)

    ans = sum(trails.values())
    return ans


def get_valid_adjacent_moves(grid: list[list[str]], curr_pos: Tuple[int, int]) -> list:
    x, y = curr_pos
    elevation = int(grid[y][x])
    adjacent = get_adjacent_moves(items, curr_pos)
    valid_moves = [
        next_pos for _, next_pos, next_val in adjacent if next_val == elevation + 1
    ]
    return valid_moves


def get_adjacent_moves(grid: list[list[str]], curr_pos: Tuple[int, int]) -> list:
    boundaries = (len(grid[0]), len(grid))
    adjacent = []
    for direction, directive in MOVES.items():
        next_pos = move(curr_pos, directive)
        if is_within_bounds(next_pos, boundaries):
            x, y = next_pos
            adjacent.append((direction, next_pos, int(grid[y][x])))
    return adjacent


def is_within_bounds(pos: Tuple[int, int], boundaries: Tuple[int, int]) -> bool:
    px, py = pos
    xb, yb = boundaries
    in_bounds = True
    if any((p < 0) for p in (px, py)):
        in_bounds = False
    if px >= xb:
        in_bounds = False
    if py >= yb:
        in_bounds = False
    return in_bounds


def move(point: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    """Apply a move in one direction"""
    result = tuple((x + y for x, y in zip(point, direction)))
    return result


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
