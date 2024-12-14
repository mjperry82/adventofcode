#!/bin/python

# 2024-12 Matt Perry mjperry82@gmail.com
# adventofcode 2024 day1

from pathlib import Path

input_file = "input"
directory = Path.cwd()

in_file = directory / input_file

num_list_1 = []
num_list_2 = []

with open(in_file, 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        line = line.split()
        num_list_1.append(int(line[0]))
        num_list_2.append(int(line[1]))

        line = file.readline()

similarity = 0

for i in range(len(num_list_1)):
    target = num_list_1[i]
    matches = [ j for j, x in enumerate(num_list_2) if x == target ]

    similarity += target * len(matches)

print(similarity)
