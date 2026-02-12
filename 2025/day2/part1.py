#! /usr/bin/python3

#Matthew Perry 2026

import csv
import re

INPUT_FILE_NAME = 'input'

def load_input(input_file):
    ranges = []
    with open(input_file, mode='r') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            ranges = line
    
    return ranges

def process_range(number_range, invalid_list):
    number_range = number_range.split('-')
    start = int(number_range[0])
    end = int(number_range[1])
    for i in range(start, end+1):
        num = str(i)
        if len(num) > 1:
            target_length = int(len(num)/2)
            invalid_list = check_pattern(num, target_length, invalid_list)
    return invalid_list

def check_pattern(num, target_length, invalid_list):        
    if len(num) % target_length == 0:
        pattern = num[:target_length]
        result = re.findall(pattern, num)
        if len(result) == len(num) / target_length and target_length == len(num) / 2:
            invalid_list.append(int(num))
            return invalid_list
                                
        
    if target_length > 2:
        invalid_list = check_pattern(num, target_length-1, invalid_list)
        return invalid_list
    else:
        return invalid_list

def main():
    ranges = load_input(INPUT_FILE_NAME)
    invalid_list = []
    for number_range in ranges:
        invalid_list = process_range(number_range, invalid_list)
    
    invalid_sum = 0
    for item in invalid_list:
        invalid_sum += item
    
    print(invalid_list)
    print(invalid_sum)

if __name__ == '__main__':
    main()