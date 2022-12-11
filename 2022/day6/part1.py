#!/bin/python3

input_file = "input.txt"

def load_input(input_file):
    input = []
    with open(input_file, 'r') as file:
        input = file.readline()
    return input

def main():
    input = load_input(input_file)
    for i in range(len(input)-3):
        temp = input[i:i+4]
        sop = True
        for char in temp:
            if temp.count(char) > 1:
                sop = False
        if sop:
            print(i+4)
            return i+4

if __name__ == "__main__":
    main()

