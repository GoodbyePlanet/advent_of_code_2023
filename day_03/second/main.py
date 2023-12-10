from file_utils.read_file import read_file


def main(engine_schematic):
    line = engine_schematic.strip().split('\n')
    num_rows = len(line)
    num_columns = len(line[0])
    gear_numbers = [[[] for _ in range(num_columns)] for _ in range(num_rows)]

    for i, row in enumerate(line):
        num = ""
        first_digit_index = None

        for j in range(0, num_columns + 1):
            if j < num_columns and line[i][j].isdigit():
                if first_digit_index is None:
                    first_digit_index = j
                num += line[i][j]
            else:
                if num == "":
                    continue
                # number found - now look for the symbol around it
                for r in range(i - 1, i + 2):  # row up, current and row down
                    for c in range(first_digit_index - 1,
                                   first_digit_index + len(num) + 1):  # checking for symbols on left and right
                        # if it's out of range continue
                        if r < 0 or r >= num_rows or c < 0 or c >= num_columns or line[r][c].isdigit():
                            continue
                        if line[r][c] == "*":
                            gear_numbers[r][c].append(num)
                num = ""
                first_digit_index = None

    sum_of_gears = 0

    for i in range(num_rows):
        for j in range(num_columns):
            part_nums = gear_numbers[i][j]
            if line[i][j] == "*" and len(part_nums) == 2:
                gear_ratio = int(part_nums[0]) * int(part_nums[1])
                sum_of_gears += gear_ratio

    print("ANSWER", sum_of_gears)
    print(gear_numbers)
    return sum_of_gears


if __name__ == "__main__":
    engine_schematic = read_file("third_day_second_input.txt")
    result = main(engine_schematic)
    print(result)
