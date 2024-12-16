#!/usr/bin/env python3

from collections import defaultdict
from aocd import get_data, submit
from collections import defaultdict
from itertools import product
import sys


data = get_data(day=10, year=2024).splitlines()
# data = open("test.txt").read().splitlines()

input_grid = []

starting_points = []
ending_points = []


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
            starting_points += [(i, j)]
        if cell == 9:
            ending_points += [(i, j)]


def find_all_paths(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    paths = []

    def dfs(x, y, path, visited):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return

        value = grid[x][y]

        # If value is visited
        if value in visited:
            return

        if path:
            previous_value = grid[path[-1][0]][path[-1][1]]
            if value <= previous_value or value - previous_value > 1:
                return

        if (x, y) == end:
            path.append((x, y))
            paths.append(path.copy())
            return

        path.append((x, y))
        visited.add((x, y))

        dfs(x + 1, y, path, visited)
        dfs(x - 1, y, path, visited)
        dfs(x, y + 1, path, visited)
        dfs(x, y - 1, path, visited)

        # Backtrack
        path.pop()
        visited.remove((x, y))

    dfs(start[0], start[1], [], set())
    return paths


nines_reached = []
for start in starting_points:
    nines_reached_for_trailhead = set()
    for end in ending_points:
        paths = find_all_paths(input_grid, start, end)
        for path in paths:
            nines_reached_for_trailhead.add(path[-1])
    nines_reached += nines_reached_for_trailhead
# print(nines_reached)
print(len(nines_reached))

# for start in starting_points:
#     print(start)


# files1 = initialize_files(data)
# files2 = deepcopy(files1)

# result1 = part1(files1)
# print(result1)
# submit(result1, part="a", day=9, year=2024)

# result2 = part2(files2)
# print(result2)
# submit(result2, part="b", day=9, year=2024)
