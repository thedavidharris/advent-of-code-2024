#!/usr/bin/env python3

from aocd import get_data, submit
from operator import mul
import re

data = get_data(day=3, year=2024)
# data = open("test2.txt").read()

matches = re.findall(r"mul\(\d+,\d+\)", data)

clean_data = re.sub(r"don't\(\).*?do\(\)|don't\(\).*", '', data)

results = eval('+'.join(re.findall(r"mul\(\d+,\d+\)", data)))
print(results)
submit(results, part="a", day=3, year=2024)

results2 = eval('+'.join(re.findall(r"mul\(\d+,\d+\)", clean_data)))
print(results2)
submit(results2, part="b", day=3, year=2024)
