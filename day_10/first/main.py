from file_utils.read_file import read_file
from collections import deque

# valid directions
# up/north    -> | 7 F
# down/south  -> | J L
# right/east  -> - J 7
# left/west   -> - L F

# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...

VALID_NORTH_DIRECTIONS = "|7F"
VALID_SOUTH_DIRECTIONS = "|JL"
VALID_EAST_DIRECTIONS = "-J7"
VALID_WEST_DIRECTIONS = "-LF"

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

# directions (row, col)
pipe_map = {
    "|": [NORTH, SOUTH],
    "-": [WEST, EAST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
    ".": []
}


def parse_grid(grid):
    return [list(row) for row in grid.split('\n')]


def get_s_row_and_col(grid):
    for ri, row in enumerate(grid):
        for ci, column in enumerate(row):
            if column == "S":
                return ri, ci
    return None


def get_s_pipe_type(grid, sp_row, sp_col):
    directions = []
    north = (sp_row + NORTH[0], sp_col + NORTH[1])
    south = (sp_row + SOUTH[0], sp_col + SOUTH[1])
    east = (sp_row + EAST[0], sp_col + EAST[1])
    west = (sp_row + WEST[0], sp_col + WEST[1])

    # check up, down, left and right and if valid pipe type add to directions array
    if grid[north[0]][north[1]] in VALID_NORTH_DIRECTIONS:
        directions.append(NORTH)
    if grid[south[0]][south[1]] in VALID_SOUTH_DIRECTIONS:
        directions.append(SOUTH)
    if grid[east[0]][east[1]] in VALID_EAST_DIRECTIONS:
        directions.append(EAST)
    if grid[west[0]][west[1]] in VALID_WEST_DIRECTIONS:
        directions.append(WEST)

    # return pipe type for start position
    return [key for key, values in pipe_map.items() if values == directions][0]


def get_valid_moves(grid, row, col):
    return [(row + dr, col + dc) for dr, dc in pipe_map[grid[row][col]]]


def main(grid_input):
    grid = parse_grid(grid_input.strip())
    start_row, start_col = get_s_row_and_col(grid)
    s_pipe_type = get_s_pipe_type(grid, start_row, start_col)

    # replace 'S' with inferred pipe type
    updated_grid = [[s_pipe_type if cell == 'S' else cell for cell in row] for row in grid]

    seen = set()
    queue = deque([(start_row, start_col)])

    while queue:
        pipe_row, pipe_col = queue.popleft()

        if (pipe_row, pipe_col) in seen:
            continue
        seen.add((pipe_row, pipe_col))

        for rr, cc in get_valid_moves(updated_grid, pipe_row, pipe_col):
            queue.append((rr, cc))

    return len(seen) // 2


if __name__ == "__main__":
    pipe_maze = read_file("first/day_10_first_input.txt")
    max_steps = main(pipe_maze)
    print(max_steps)
