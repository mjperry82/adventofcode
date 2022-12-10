#!/bin/python3

input_file = "input.txt"

def load_rucksacks(input_file):
    rucksacks = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            rucksacks.append(line.strip())

    return rucksacks

def score_char(char,lower_list):
    if char in lower_list:
        return ord(char) - 96
    else:
        return ord(char) - 38
    
def find_common_char(group_sacks):
    common_list = []
    for char in group_sacks[0]:
        if char in group_sacks[1] and char not in common_list:
            common_list.append(char)
    for char in common_list:
        if char in group_sacks[2]:
            return char

def main():
    lower_list = []
    for i in range(97,123,1):
        lower_list.append(chr(i))
    
    rucksacks = load_rucksacks(input_file)
    score = 0
    for num in range(0,len(rucksacks),3):
        char = find_common_char(rucksacks[num:num+3])
        score += score_char(char,lower_list)

    print(score)

if __name__ == "__main__":
    main()

