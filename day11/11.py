#!/usr/bin/env python3

from aocd import get_data, submit
from functools import cache

data = get_data(day=11, year=2024).strip().split()
# data = open("test.txt").read().strip().split()

data = list(map(int, data))


@cache
def blink_stone(stone, iterations_left):
    if iterations_left == 0:
        return 1

    if stone == 0:
        return blink_stone(1, iterations_left - 1)

    stone_string = str(stone)
    length = len(stone_string)

    if length % 2 == 0:
        mid = length // 2
        left, right = int(stone_string[:mid]), int(stone_string[mid:])
        return blink_stone(left, iterations_left - 1) + blink_stone(right, iterations_left - 1)

    else:
        return blink_stone(stone * 2024, iterations_left - 1)


part1 = sum(blink_stone(stone, 25) for stone in data)
print(part1)
submit(part1, part="a", day=11, year=2024)

part2 = sum(blink_stone(stone, 75) for stone in data)
print(part2)
submit(part2, part="b", day=11, year=2024)
