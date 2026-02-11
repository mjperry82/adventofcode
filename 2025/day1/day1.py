#! /usr/bin/python3

#Matthew Perry 2026

INPUT_FILE_NAME = 'input'

def load_input(input_file):
    movements = []
    with open(input_file, mode='r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            movements.append(line)

            line = file.readline()
    
    return movements


def move_dial(dial, move):
    print(f"start dial: {dial} move: {move}")
    direction = move[0]
    move = int(move[1:])

    if direction == 'R':
        for i in range(move):
            dial += 1
            if dial > 99:
                dial = 0
    else:
        for i in range(move):
            dial -= 1
            if dial < 0:
                dial = 99

    print(f"end dial: {dial}")

    return dial

def main():
    movements = load_input(INPUT_FILE_NAME)
    dial = 50

    count = 0
    for move in movements:
        dial = move_dial(dial, move)
        if dial == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()