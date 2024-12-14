#!/bin/python

# 2024-12 Matt Perry mjperry82@gmail.com
# adventofcode 2024 day1

from pathlib import Path

input_file = "input"
directory = Path.cwd()

in_file = directory / input_file

report_list = []

with open(in_file, 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        line = line.split()
        line_list = []
        for i in line:
            line_list.append(int(i))
        report_list.append(line_list)
        line = file.readline()

safe_count = 0

for line in report_list:
    safe = True
    increasing = None
    count = 0

    for j in range(len(line)-1):
        diff = line[j] - line[j+1]
        if count == 0:
            if diff >= 0:
                increasing = True
            else:
                increasing = False
        elif ( diff >= 0 and increasing == False ) or ( diff < 0 and increasing ):
             safe = False

        if abs(diff) > 3 or diff == 0:
            safe = False
        count += 1
    
    if safe:
        safe_count += 1

print(safe_count)
