#!/usr/bin/env python3

from aocd import get_data, submit
from operator import mul, add


def concat(x, y): return int(str(x) + str(y))


data = get_data(day=7, year=2024).splitlines()
# data = open("test.txt").read().splitlines()


def solve(data, operators):
    total_sum = 0
    for line in data:

        target, first_number, * \
            other_numbers = map(int, line.replace(':', '').split())

        possible_values = [first_number]

        for number in other_numbers:
            possible_values = [operation(x, number)
                               for x in possible_values for operation in operators]

        # Check if target is in possible values and add to the total sum
        if target in possible_values:
            total_sum += target

    return total_sum


part1 = solve(data, [mul, add])
print(part1)
submit(part1, part="a", day=7, year=2024)

part2 = solve(data, [mul, add, concat])
print(part2)
submit(part2, part="b", day=7, year=2024)
