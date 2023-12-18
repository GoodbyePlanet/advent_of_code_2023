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

    seeds_ranges = []
    seeds = list(seeds)

    for i in range(0, len(seeds), 2):
        seeds_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

    for m in maps:
        ranges = []
        for x in m:
            ranges.append(list(map(int, x[0].split())))

        #  logic copied from https://www.youtube.com/watch?v=NmxHw_bHhGM
        locations = []
        while len(seeds_ranges) > 0:
            seed_start, seed_length = seeds_ranges.pop()
            for destination, source, range_len in ranges:
                overlap_start = max(seed_start, source)
                overlap_end = min(seed_length, source + range_len)

                if overlap_start < overlap_end:
                    locations.append((overlap_start - source + destination, overlap_end - source + destination))
                    if overlap_start > seed_start:
                        seeds_ranges.append((seed_start, overlap_start))
                    if seed_length > overlap_end:
                        seeds_ranges.append((overlap_end, seed_length))
                    break
            else:
                locations.append((seed_start, seed_length))
        seeds_ranges = locations

    return min(locations)[0]


if __name__ == "__main__":
    almanac = read_file("day_05_second_input.txt")
    min_location = main(almanac)
    print(min_location)
