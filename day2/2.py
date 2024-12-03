#!/usr/bin/env python3

from aocd import get_data, submit
from itertools import combinations

data = get_data(day=2, year=2024).splitlines()
# data = open("test.txt").read().splitlines()

reports = [[int(x) for x in row.split()] for row in data]


def is_safe(report):
    zipped = zip(report, report[1:])
    diffs = set([b - a for a, b in zipped])

    return diffs.issubset({1, 2, 3}) or diffs.issubset({-1, -2, -3})


safe = sum(is_safe(report) for report in reports)
print(safe)
submit(safe, part="a", day=2, year=2024)

safe = sum(any(is_safe(combo) for combo in combinations(
    report, len(report) - 1)) for report in reports)
print(safe)
submit(safe, part="b", day=2, year=2024)
