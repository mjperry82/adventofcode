#!/bin/python3

input_file = "input.txt"

def load_rucksacks(input_file):
    rucksacks = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            rucksacks.append(line.strip())

    return rucksacks

def score_duplicate(char,lower_list):
    if char in lower_list:
        return ord(char) - 96
    else:
        return ord(char) - 38

def process_rucksack(rucksack,lower_list):
    print(rucksack)
    half_length = int(len(rucksack) / 2)
    compartment1 = rucksack[:half_length]
    compartment2 = rucksack[half_length:]
    
    score = 0
    found_list = []
    for char in compartment1:
        if char in compartment2 and char not in found_list:
            print(char)
            found_list.append(char)
            score += score_duplicate(char,lower_list)
    print(score)
    return score

def main():
    lower_list = []
    for i in range(97,123,1):
        lower_list.append(chr(i))
    
    rucksacks = load_rucksacks(input_file)
    score = 0
    for rucksack in rucksacks:
        score += process_rucksack(rucksack,lower_list)

    print(score)

if __name__ == "__main__":
    main()

