#!/usr/bin/env python3

from aocd import get_data, submit
from collections import defaultdict
from functools import cmp_to_key

data = get_data(day=5, year=2024)
# data = open("test.txt").read()

data = data.split("\n\n")
ordering_section = data[0].splitlines()
page_section = [list(map(int, line.split(",")))
                for line in data[1].splitlines()]


rules = defaultdict(list)
for rule in ordering_section:
    first, second = map(int, rule.split("|"))
    rules[first].append(second)


def order_page(a, b):
    if a in rules[b]:
        return 1
    elif b in rules[a]:
        return -1
    else:
        return 0


mid_correct_sum = 0
mid_incorrect_sum = 0

for pages in page_section:
    sorted_pages = sorted(pages, key=cmp_to_key(order_page))
    mid_index = len(pages) // 2

    if pages == sorted_pages:
        mid_correct_sum += pages[mid_index]
    else:
        mid_incorrect_sum += sorted_pages[mid_index]

print(mid_correct_sum)
print(mid_incorrect_sum)

submit(mid_correct_sum, part="a", day=5, year=2024)
submit(mid_incorrect_sum, part="b", day=5, year=2024)
