#!/usr/bin/env python3

from collections import defaultdict
from aocd import get_data, submit
import sys


data = get_data(day=10, year=2024).splitlines()
# data = open("test.txt").read().splitlines()

grid = {}


def set_to_int_min_if_not_int(value):
    # Hacky function to cover for putting dots in the test inputs
    try:
        int_value = int(value)
        return int_value
    except (ValueError, TypeError):
        return -sys.maxsize - 1


for i, row in enumerate(data):
    for j, cell in enumerate(row):
        grid[complex(i, j)] = set_to_int_min_if_not_int(cell)

DIRECTIONS = [1, -1, 1j, -1j]


def search_trailhead(grid, pos, seen, height):
    if pos in grid and grid[pos] == height:
        if height < 9 or (part == "a" and pos in seen):
            # Explore all four directions
            return sum(search_trailhead(grid, pos + n, seen, height + 1) for n in DIRECTIONS)
        seen.add(pos)
        return 1
    return 0


def calculate_trailhead_scores(grid, part):
    """Calculate the sum of scores for all trailheads."""
    return sum(search_trailhead(grid, pos, set(), 0) for pos in grid if grid[pos] == 0)


# Calculate scores for both parts
for part in ["a", "b"]:
    score = calculate_trailhead_scores(grid, part)
    print(f"Part {part}: {score}")
    submit(score, part=part, day=10, year=2024)
