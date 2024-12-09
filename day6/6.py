#!/usr/bin/env python3

from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=6, year=2024)
data = open("test.txt").read()

data = data.splitlines()

# Default value is None, indicating out of bounds
grid = defaultdict(lambda: None)
start = None

for i, row in enumerate(data):
    for j, cell in enumerate(row):
        grid[complex(i, j)] = cell
        if cell == "^":
            start = complex(i, j)
            grid[start] = "."  # Replace start position with empty space


def print_grid(g):
    min_x = int(min(p.real for p in g))
    max_x = int(max(p.real for p in g))
    min_y = int(min(p.imag for p in g))
    max_y = int(max(p.imag for p in g))

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print(g[complex(i, j)], end="")
        print()


def walk_grid(grid, position):
    direction = -1  # Initial direction (facing upward)
    turn_value = -1j  # Use -1j for clockwise rotation (right turn)

    visited_and_direction = {(position, direction)}  # Set of visited positions

    while True:
        new_pos = position + direction

        if grid[new_pos] == ".":
            visited_and_direction.add((new_pos, direction))
            position = new_pos
        elif grid[new_pos] == "#":
            direction *= turn_value  # Turn right
        elif grid[new_pos] is None:  # Exit map
            return {p for p, _ in visited_and_direction}, (new_pos, direction) in visited_and_direction


walk_grid_result = walk_grid(grid, start)

print(walk_grid_result)

visited_and_direction_answer = walk_grid_result[0]
answer1 = len(walk_grid_result[0])
print(answer1)
# submit(answer1, part="a", day=6, year=2024)


# Part 2
