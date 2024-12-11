""" https://adventofcode.com/2022/day/2 """

winners = [
    ("C", "A"),
    ("B", "C"),
    ("A", "B"),
]


def part1():
    """
    'A': 'Rock'     -> 1 point
    'B': 'Paper'    -> 2 points
    'C': 'Scissors' -> 3 points

    'Loss'          -> 0 points
    'Draw'          -> 3 points
    'Win'           -> 6 points plus your_move Rock/Paper/Scissor points
    """
    with open("data/day2_input.txt", "r") as f:
        items = f.read().splitlines()
    data = []
    for item in items:
        opp_move, your_move = (
            item.replace("X", "A").replace("Y", "B").replace("Z", "C").split(" ")
        )
        score = 0  # Lose
        if opp_move == your_move:
            score += 3  # Draw
        if (opp_move, your_move) in winners:
            score += 6  # Win
        your_move_points = ord(your_move.lower()) - 96
        score += your_move_points
        data.append(score)
    return sum(data)


def part2():
    """
    X -> means you need to lose,
    Y -> means you need to draw
    Z -> means you need to win
    """
    with open("data/day2_input.txt", "r") as f:
        items = f.read().splitlines()
    data = []
    for item in items:
        opp_move, outcome = item.split(" ")
        your_move = None
        score = 0
        if outcome == "X":  # Lose
            your_move = [winner[0] for winner in winners if opp_move == winner[1]].pop()
        if outcome == "Y":  # Draw
            your_move = opp_move
            score += 3
        if outcome == "Z":  # Win
            your_move = [winner[1] for winner in winners if opp_move == winner[0]].pop()
            score += 6
        your_move_points = ord(your_move.lower()) - 96
        score += your_move_points
        data.append(score)
    return sum(data)


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
