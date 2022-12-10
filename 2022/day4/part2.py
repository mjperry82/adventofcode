#!/bin/python3

input_file = "input.txt"

def load_input(input_file):
    input = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            input.append(line.strip())

    return input

def create_lists(line):
    line = line.split(',')
    list_holder = []

    for i in range(len(line)):
        list_holder.append([])
        myrange = line[i].split('-')
        for j in range(int(myrange[0]),int(myrange[1])+1):
            list_holder[i].append(j)

    return list_holder[0],list_holder[1]

def process_line(line):
    list1,list2 = create_lists(line)
    for num in list1:
        if num in list2:
            return 1
    return 0

def main():
    input = load_input(input_file)

    score = 0
    for line in input:
        score += process_line(line)
    print(score)

if __name__ == "__main__":
    main()

