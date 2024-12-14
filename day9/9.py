#!/usr/bin/env python3

from collections import defaultdict
from aocd import get_data, submit
from copy import deepcopy


class File:
    def __init__(self, identifier, size):
        self.identifier = identifier
        self.size = size

    def __repr__(self):
        return f"<Value: {self.identifier}, Size: {self.size}>"


def initialize_files(data):
    return [File(i // 2 + 1 if i % 2 else 0, size) for i, size in enumerate(map(int, data), 1)]


def compute_checksum(files):
    pos, checksum = 0, 0
    for file in files:
        for _ in range(file.size):
            if file.identifier != 0:
                checksum += pos * (file.identifier - 1)
            pos += 1
    return checksum


def part1(files):
    l, r = 1, len(files) - 1
    while l < len(files) and r > 0:
        assert files[l].identifier == 0

        if files[r].size <= files[l].size:
            files[l].size -= files[r].size
            files.insert(l, files.pop(r))
            files.pop()
            r -= 1
            l += 1
        else:
            files[l].identifier += files[r].identifier
            files[r].size -= files[l].size
            l += 2

    return compute_checksum(files)


def part2(files):
    r = len(files) - 1
    while r > 0:
        l = 1

        while r > 0 and files[r].identifier == 0:
            r -= 1

        if r == 0:
            break

        while l < r and not (files[l].identifier == 0 and files[l].size >= files[r].size):
            l += 1

        if l < r:
            files[l].size -= files[r].size
            files[r - 1].size += files[r].size
            files.insert(l, files.pop(r))

        r -= 1

    return compute_checksum(files)


data = get_data(day=9, year=2024)
files1 = initialize_files(data)
files2 = deepcopy(files1)

result1 = part1(files1)
print(result1)
submit(result1, part="a", day=9, year=2024)

result2 = part2(files2)
print(result2)
submit(result2, part="b", day=9, year=2024)
