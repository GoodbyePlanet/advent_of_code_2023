from file_utils.read_file import read_file


def main(boat_races_input):
    lines = boat_races_input.splitlines()
    times = list(map(int, lines[0].split("Time:")[1].strip().split()))
    record_distances = list(map(int, lines[1].split("Distance:")[1].strip().split()))

    ways_to_win = []

    for index, time in enumerate(times):
        record = record_distances[index]
        ways = []

        for hold in range(1, time + 1):
            record_achieved = hold * (time - hold)

            if record_achieved > record:
                ways.append(hold)

        ways_to_win.append(len(ways))

    mult_of_the_ways = 1
    for w in ways_to_win:
        mult_of_the_ways *= w

    return mult_of_the_ways


if __name__ == "__main__":
    boat_races = read_file("day_06_first_input.txt")
    multiple_of_ways_to_win = main(boat_races)
    print(multiple_of_ways_to_win)
