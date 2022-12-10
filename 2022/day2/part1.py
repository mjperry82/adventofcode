#!/bin/python3

input_file = "input.txt"

def load_input(input_file):
    input = []
    
    with open(input_file, 'r') as file:
        for line in file.readlines():
            input.append(line.strip().split(' '))

    return input

def process_line(line):
    if line[0] == 'A':
        if line[1] == 'X':
            return 4
        elif line[1] == 'Y':
            return 8
        elif line[1] == 'Z':
            return 3
    elif line[0] == 'B':
        if line[1] == 'X':
            return 1
        elif line[1] == 'Y':
            return 5
        elif line[1] == 'Z':
            return 9
    elif line[0] == 'C':
        if line[1] == 'X':
            return 7
        elif line[1] == 'Y':
            return 2
        elif line[1] == 'Z':
            return 6

def main():
    input = load_input(input_file)
    
    score = 0
    for line in input:
        score += process_line(line)
    
    print(score)

if __name__ == "__main__":
    main()
