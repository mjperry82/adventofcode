#!/bin/python3

# Matt Perry mjperry82@gmail.com

input_file = 'input.txt'

def main():
    # load input file to input
    intput = []
    with open(input_file, 'r') as file:
        input = file.readlines()
    
    max = 0
    temp = 0
    count = 1
    for line in input:
        if line.strip() != '':
            temp += int(line.strip())
        else:
            if temp > max:
                max = temp
                print(f'max: {max} count: {count}')
            temp = 0
            count += 1

    print(max)

if __name__ == "__main__":
    main()
