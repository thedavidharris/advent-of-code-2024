#!/usr/bin/env python3

from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=6, year=2024)
# data = open("test.txt").read()

data = data.splitlines()

# Default value is None, indicating out of bounds
grid = {}
start = None

for i, row in enumerate(data):
    for j, cell in enumerate(row):
        grid[complex(i, j)] = cell
        if cell == "^":
            start = complex(i, j)


def walk_grid(grid, start_position):
    direction = -1  # Initial direction (facing upward)
    turn_value = -1j  # Use -1j for clockwise rotation (right turn)

    position = start_position
    visited_and_direction = set()

    while (position, direction) not in visited_and_direction and position in grid:
        visited_and_direction.add((position, direction))
        new_position = position + direction
        if grid.get(new_position) == "#":
            direction *= turn_value
        else:
            position = new_position
    return {p for p, _ in visited_and_direction}, (position, direction) in visited_and_direction


walk_grid_result = walk_grid(grid, start)

visited_and_direction_answer = walk_grid_result[0]
answer1 = len(walk_grid_result[0])
print(answer1)
submit(answer1, part="a", day=6, year=2024)

answer2 = sum(walk_grid(grid | {position: '#'}, start)[
              1] for position in visited_and_direction_answer if position != start)
print(answer2)
submit(answer2, part="b", day=6, year=2024)
