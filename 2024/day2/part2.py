#!/bin/python

# 2024-12 Matt Perry mjperry82@gmail.com
# adventofcode 2024 day1

from pathlib import Path

input_file = "input"
directory = Path.cwd()

in_file = directory / input_file

def load_report_list():
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

    return report_list

def is_safe(num_list):
    safe = True
    increasing = None
    count = 0

    for j in range(len(num_list)-1):
        diff = num_list[j] - num_list[j+1]
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

    return safe

def process_num_list(num_list):
    if is_safe(num_list):
        return 1
    else:
        for i in range(len(num_list)):
            temp_list = num_list.copy()
            temp_list.pop(i)
            if is_safe(temp_list):
                return 1

    return 0

def main():
    report_list = load_report_list()
    safe_count = 0

    for num_list in report_list:
        safe_count += process_num_list(num_list)

    print(safe_count)

if __name__ == "__main__":
    main()

