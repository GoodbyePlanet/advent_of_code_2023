from file_utils.read_file import read_file


def main(engine_schematic):
    line = engine_schematic.strip().split('\n')
    num_rows = len(line)
    num_columns = len(line[0])
    part_numbers = []

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
                        if line[r][c] != "." and not line[r][c].isdigit():
                            part_numbers.append(int(num))
                num = ""
                first_digit_index = None

    return sum(part_numbers)


if __name__ == "__main__":
    engine_schematic = read_file("third_day_first_input.txt")
    result = main(engine_schematic)
    print(result)
