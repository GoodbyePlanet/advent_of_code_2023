from file_utils.read_file import read_file

red_max = 12
green_max = 13
blue_max = 14


def main(file):
    power_of_min_set_games = []

    for line in file.strip().split("\n"):
        games = line.split(":")[-1].split(";")

        curr_red = 0
        curr_green = 0
        curr_blue = 0

        for game in games:
            g = game.split(",")
            for x in g:
                r = x.split()
                if "red" in x and int(r[0]) > curr_red:
                    curr_red = int(r[0])
                if "green" in x and int(r[0]) > curr_green:
                    curr_green = int(r[0])
                if "blue" in x and int(r[0]) > curr_blue:
                    curr_blue = int(r[0])

        power_of_set = curr_red * curr_green * curr_blue
        power_of_min_set_games.append(power_of_set)

    print(power_of_min_set_games)
    return sum(map(int, power_of_min_set_games))


if __name__ == "__main__":
    input_file = read_file("second_day_second_input.txt")
    allowed_games_sum = main(input_file)
    print(f"Allowed games sum {allowed_games_sum}")
