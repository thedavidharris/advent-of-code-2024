#!/usr/bin/env python3

from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=4, year=2024).splitlines()
# data = open("test.txt").read().splitlines()

grid = defaultdict(lambda: '.')

for i in range(len(data)):
    for j in range(len(data[i])):
        grid[complex(i, j)] = data[i][j]

directions = {1, -1, 1j, -1j, -1+1j, -1-1j, 1-1j, 1+1j}

coords = list(grid.keys())

# Part 1
count = 0

for c in coords:
    for d in directions:
        word = grid[c] + grid[c+d] + grid[c+2*d] + grid[c+3*d]
        if word == "XMAS":
            count += 1

print(count)
submit(count, part="a", day=4, year=2024)

# Part 2
count = 0
for c in coords:
    if grid[c] != "A":
        continue
    slope1, slope2 = complex(1, 1), complex(1, -1)
    a = {grid[c+slope1], grid[c-slope1]}
    b = {grid[c+slope2], grid[c-slope2]}
    if a == b == {"M", "S"}:
        count += 1
print(count)
submit(count, part="b", day=4, year=2024)
