# https://adventofcode.com/2025/day/1

'''
"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually 
supposed to count the number of times any click causes the dial to point at 0, 
regardless of whether it happens during a rotation or at the end of one.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def rotate_dial(sequence):
    position = 50 # starting position
    password = 0
    for instruction in sequence:
        direction = str(instruction[0])
        distance = int(instruction[1:])
        if direction == 'R':
            position += distance
            password += abs(position) // 100
        else: # position == 'L'
            if position == 0:
                gap = 100
            else:
                gap = position
            if distance >= gap and position != 0:
                password += 1
            position -= distance
            if position < 0:
                password += abs(position) // 100
        testposition = position
        position = abs(position % 100) # 99/0 circular position correction
        print('instruction', instruction, '\tposition', testposition, position, '\tpassword', password)
    print("password:", password)

def main():
    print('\n============================\nAdvent of Code 2025 - Day 1b\n============================\n')
    f = '01.csv'
    #f = '01test.csv'
    sequence = read_input(f) # ['R26', 'L12', 'L47', 'L2', 'R15', ...]
    rotate_dial(sequence)

main()
