from file_utils.read_file import read_file


def get_empty_rows(grid):
    return [r for r, row in enumerate(grid) if all(char == "." for char in row)]


def get_empty_columns(grid):
    return [col for col in range(len(grid[0])) if all(row[col] == "." for row in grid)]


def get_galaxies(grid):
    return [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"]


def main(input_image):
    grid = input_image.splitlines()

    empty_rows = get_empty_rows(grid)
    empty_columns = get_empty_columns(grid)
    galaxies = get_galaxies(grid)

    scale = 2
    total = 0

    for i, (g_row1, g_col1) in enumerate(galaxies):
        for (g_row2, g_col2) in galaxies[:i]:
            for row in range(min(g_row1, g_row2), max(g_row1, g_row2)):
                if row in empty_rows:
                    total += scale
                else:
                    total += 1
            for col in range(min(g_col1, g_col2), max(g_col1, g_col2)):
                if col in empty_columns:
                    total += scale
                else:
                    total += 1

    return total


if __name__ == "__main__":
    image = read_file("day_11_first_input.txt")
    sum_of_lengths = main(image)
    print(sum_of_lengths)
