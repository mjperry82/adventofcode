#!/bin/python3

# Matt Perry mjperry82@gmail.com

input_file = 'input.txt'

def set_max(max1,max2,max3,temp):
    if temp > max1:
        max3 = max2
        max2 = max1
        max1 = temp
    elif temp > max2:
        max3 = max2
        max2 = temp
    elif temp > max3:
        max3 = temp

    return max1, max2, max3


def main():
    # load input file to input
    intput = []
    with open(input_file, 'r') as file:
        input = file.readlines()
    
    max1 = 0
    max2 = 0
    max3 = 0
    temp = 0
    for line in input:
        if line.strip() != '':
            temp += int(line.strip())
        else:
            max1,max2,max3 = set_max(max1,max2,max3,temp)
            temp = 0

    print(f'max1: {max1}\nmax2: {max2}\nmax3: {max3}\nTotal: {max1+max2+max3}')

if __name__ == "__main__":
    main()
