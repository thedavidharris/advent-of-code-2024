#!/usr/bin/env python3

from aocd import get_data, submit

data = get_data(day=6, year=2024).splitlines()

grid = {}
start_position = None

for i, row in enumerate(data):
    for j, cell in enumerate(row):
        grid[complex(i, j)] = cell
        if cell == "^":
            start_position = complex(i, j)


def walk_grid(grid, start):
    direction = -1  # Initial direction (upward)
    turn_clockwise = -1j  # Right turn

    position = start
    visited_positions = set()

    while (position, direction) not in visited_positions and position in grid:
        visited_positions.add((position, direction))
        next_position = position + direction
        if grid.get(next_position) == "#":
            direction *= turn_clockwise
        else:
            position = next_position

    visited_cells = {pos for pos, _ in visited_positions}
    is_cyclic = (position, direction) in visited_positions
    return visited_cells, is_cyclic


# Walk the grid and get results
visited_cells, is_cyclic = walk_grid(grid, start_position)

# Part A
answer1 = len(visited_cells)
print(answer1)
submit(answer1, part="a", day=6, year=2024)

# Part B
answer2 = sum(walk_grid(grid | {pos: '#'}, start_position)[
              1] for pos in visited_cells if pos != start_position)
print(answer2)
submit(answer2, part="b", day=6, year=2024)
