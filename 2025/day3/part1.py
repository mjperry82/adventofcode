#! /usr/bin/python3

#Matthew Perry 2026

INPUT_FILE_NAME = 'input'

def load_input(input_file):
    input = []
    with open(input_file, mode='r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            input.append(line)

            line = file.readline()
    
    return input

def process_input(input):
    joltage = []
    for line in input:
        joltage.append(find_highest(line))
    return joltage

def find_highest(line):
    max = 0
    position = 0
    for i in range(len(line)-1):
        if int(line[i]) > max:
            max = int(line[i])
            pos = i
    
    the_rest = line[pos+1:]
    max2 = 0
    pos2 = 0
    for i in range(len(the_rest)):
        if int(the_rest[i]) > max2:
            max2 = int(the_rest[i])
            pos2 = i
    
    print(f"line: {line} max: {max} pos: {pos}")
    print(f"the_rest: {the_rest} max2: {max2} pos2: {pos2}")

    return line[pos] + the_rest[pos2]            

def main():
    input = load_input(INPUT_FILE_NAME)
    joltage = process_input(input)

    sum = 0
    for jolt in joltage:
        sum += int(jolt)

    print(sum)

if __name__ == '__main__':
    main()