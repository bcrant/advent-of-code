import pprint


year, day = 2023, 2


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    tgt = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    games = {}
    for item in items:
        game_id, pulls = str(item).split(":")
        pulls = [
            pull.strip() 
            for pull in pulls.replace(";", ",").split(",")
        ]
        game_cnt = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        # Get max per each bag
        for pull in pulls:
            cnt, color = pull.split(" ")
            cnt = int(cnt)
            if cnt > game_cnt.get(color):
                game_cnt[color] = cnt
        games[game_id] = game_cnt

    # Count only bags matching target
    sum_ids = 0
    for game_id, game in games.items():
        if all(
            game[color] <= tgt[color]
            for color in ("red", "green", "blue")
        ):
            _id = int(game_id.replace("Game ", ""))
            sum_ids += _id
    return sum_ids


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    games = {}
    for item in items:
        game_id, pulls = str(item).split(":")
        pulls = [
            pull.strip() 
            for pull in pulls.replace(";", ",").split(",")
        ]
        game_cnt = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        # Get max per each bag
        for pull in pulls:
            cnt, color = pull.split(" ")
            cnt = int(cnt)
            if cnt > game_cnt.get(color):
                game_cnt[color] = cnt
        x,y,z = game_cnt.values()
        games[game_id] = x*y*z

    return sum(games.values())


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")

