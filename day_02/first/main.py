from file_utils.read_file import read_file

red_max = 12
green_max = 13
blue_max = 14


def main(file):
    allowed_game_ids = []

    for line in file.strip().split("\n"):
        game_id = line.split(":")[0].split()[-1]
        games = line.split(":")[-1].split(";")

        red = True
        green = True
        blue = True

        for game in games:
            g = game.split(",")
            for x in g:
                r = x.split()
                if "red" in x and int(r[0]) > red_max:
                    red = False
                if "green" in x and int(r[0]) > green_max:
                    green = False
                if "blue" in x and int(r[0]) > blue_max:
                    blue = False

        if red and green and blue:
            allowed_game_ids.append(game_id)

    print(allowed_game_ids)
    return sum(map(int, allowed_game_ids))


if __name__ == "__main__":
    input_file = read_file("second_day_first_input.txt")
    allowed_games_sum = main(input_file)
    print(f"Allowed games sum {allowed_games_sum}")
