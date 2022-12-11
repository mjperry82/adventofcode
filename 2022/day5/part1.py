#!/bin/python3

input_file = "input.txt"

def load_input(input_file):
    input = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            input.append(line)

    return input

def create_stacks(input):
    stacks = []
    for num in range(9):
        stacks.append([])
    for line in input:
        count = 0
        for i in range(1,35,4):
            if line[i:i+1] != ' ':
                stacks[count].append(line[i:i+1])
            count += 1
    return stacks

def create_movements(input):
    movements = []
    for line in input:
        line = line.split()
        temp = [
                int(line[1]),
                int(line[3]),
                int(line[5])
                ]
        movements.append(temp)
    return movements

def process_move(stacks,move):
    temp = stacks[move[1]-1][:move[0]]
    for char in temp:
        stacks[move[1]-1].remove(char)
        stacks[move[2]-1].insert(0,char)
    return stacks

def get_top(stacks):
    top = []
    for stack in stacks:
        if len(stack) > 0:
            top.append(stack[0])
        else:
            top.append(' ')
    return top


def main():
    input = load_input(input_file)
    stacks = create_stacks(input[:8])
    movements = create_movements(input[10:])
    for move in movements:
        stacks = process_move(stacks,move)
    top = get_top(stacks)
    print("".join(top))

if __name__ == "__main__":
    main()

