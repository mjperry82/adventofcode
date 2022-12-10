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
    if list1[:1] <= list2[:1] and list1[-1:] >= list2[-1:]:
        return 1
    elif list2[:1] <= list1[:1] and list2[-1:] >= list1[-1:]:
        return 1
    else:
        return 0

def main():
    input = load_input(input_file)

    score = 0
    for line in input:
        score += process_line(line)
    print(score)

if __name__ == "__main__":
    main()

