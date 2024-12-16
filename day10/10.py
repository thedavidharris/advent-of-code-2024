#!/usr/bin/env python3

from collections import defaultdict
from aocd import get_data, submit
from collections import defaultdict
from itertools import product
import sys


data = get_data(day=10, year=2024).splitlines()
# data = open("test.txt").read().splitlines()

input_grid = []
start_points = []
end_points = []


# Parse input

def set_to_int_min_if_not_int(value):
    # Hacky function to cover for putting dots in the test inputs
    try:
        int_value = int(value)
        return int_value
    except (ValueError, TypeError):
        return -sys.maxsize - 1


for line in data:
    input_row = [set_to_int_min_if_not_int(x) for x in list(line)]
    input_grid.append(input_row)

for i, line in enumerate(input_grid):
    for j, cell in enumerate(line):
        if cell == 0:
            start_points += [(i, j)]
        if cell == 9:
            end_points += [(i, j)]


# DFS to find all valid paths from start to end
def find_all_paths(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    paths = []

    def dfs(x, y, path, visited):
        if not (0 <= x < rows and 0 <= y < cols):
            return

        value = grid[x][y]
        if (x, y) in visited or (path and value != grid[path[-1][0]][path[-1][1]] + 1):
            return

        if (x, y) == end:
            paths.append(path + [(x, y)])
            return

        path.append((x, y))
        visited.add((x, y))

        # Explore all four directions
        dfs(x + 1, y, path, visited)
        dfs(x - 1, y, path, visited)
        dfs(x, y + 1, path, visited)
        dfs(x, y - 1, path, visited)

        # Backtrack
        path.pop()
        visited.remove((x, y))

    dfs(start[0], start[1], [], set())
    return paths


# Part 1
nines_reached = []
for start in start_points:
    nines_reached_for_trailhead = set()
    for end in end_points:
        paths = find_all_paths(input_grid, start, end)
        for path in paths:
            nines_reached_for_trailhead.add(path[-1])
    nines_reached += nines_reached_for_trailhead

part1 = len(nines_reached)
print(f"Part 1: {part1}")
submit(part1, part="a", day=10, year=2024)

# Part 2

total_rating = 0
for start in start_points:
    rating = 0
    for end in end_points:
        paths = find_all_paths(input_grid, start, end)
        rating += len(paths)
    total_rating += rating

print(f"Part 2: {total_rating}")
submit(total_rating, part="b", day=10, year=2024)
