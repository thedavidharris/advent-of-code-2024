#!/usr/bin/env python3

from aocd import get_data, submit
from collections import Counter

data = get_data(day=1, year=2024).split()
# data = open("test.txt").read().split()

distance = sum(abs(int(x) - int(y))
               for x, y in zip(sorted(data[::2]), sorted(data[1::2])))

submit(distance, part="a", day=1, year=2024)

left = [int(x) for x in data[::2]]
right = [int(x) for x in data[1::2]]

counts = Counter(right)

similarity = sum(item * counts[item] for item in left)

submit(similarity, part="b", day=1, year=2024)
