from file_utils.read_file import read_file


def process_maps(list_of_maps):
    maps_nums = []
    curr_sublist = []

    for item in list_of_maps:
        if item != "":
            curr_sublist.append([item])
        elif curr_sublist:
            maps_nums.append(curr_sublist)
            curr_sublist = []

    if curr_sublist:
        maps_nums.append(curr_sublist)

    maps = [el[1:] for el in maps_nums]

    return maps


def main(almanac_input):
    lines = almanac_input.strip()
    seeds = map(int, almanac_input.splitlines()[0].split(":")[1].split())
    maps = process_maps(lines.splitlines()[1:])

    locations = []

    for seed in seeds:
        curr_seed = seed
        for map_item in maps:
            for x in map_item:
                destination, source, range_len = map(int, x[0].split())
                if source <= curr_seed < source + range_len:  # seed >= source and seed < source + range_len
                    curr_seed = destination + (curr_seed - source)
                    break

        locations.append(curr_seed)

    return min(locations)


if __name__ == "__main__":
    almanac = read_file("day_05_first_input.txt")
    min_location = main(almanac)
    print(min_location)
