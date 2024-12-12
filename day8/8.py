#!/usr/bin/env python3

from collections import defaultdict
from aocd import get_data, submit
from itertools import permutations

data = get_data(day=8, year=2024).splitlines()
# data = open("test.txt").read().splitlines()

N, M = len(data), len(data[0])  # rows and columns

# Collecting antenna positions indexed by character
antennas = defaultdict(list)
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell != ".":
            antennas[cell].append(complex(i, j))


def is_inside(pos):
    return 0 <= pos.real < N and 0 <= pos.imag < M


# Calculate antinodes
antinodes1 = set()
antinodes2 = set()

for locations in antennas.values():
    for a, b in permutations(locations, 2):
        v = a - b
        u = b - a
        antinodes1.update({a + u * 2, b + v * 2})
        antinodes2.update(a + i * u for i in range(1, max(N, M)))
        antinodes2.update(b + i * v for i in range(1, max(N, M)))

# Calculate and submit results
part1 = sum(is_inside(antinode) for antinode in antinodes1)
print(part1)
submit(part1, part="a", day=8, year=2024)

part2 = sum(is_inside(antinode) for antinode in antinodes2)
print(part2)
submit(part2, part="b", day=8, year=2024)
