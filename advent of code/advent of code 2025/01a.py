# https://adventofcode.com/2025/day/1

'''
The attached document (your puzzle input) contains a sequence of rotations, 
one per line, which tell you how to open the safe. 
A rotation starts with an L or R which indicates whether the rotation should be 
to the left (toward lower numbers) or to the right (toward higher numbers). 
Then, the rotation has a distance value which indicates 
how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. 
After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. 
Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. 
After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

Input file: 01a.csv
Sample of input:
R26
L12
L47
L2
R15

You could follow the instructions, but your recent required official North Pole 
secret entrance security training seminar taught you that the safe is actually a decoy. 
The actual password is the number of times the dial is left 
pointing at 0 after any rotation in the sequence.
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
        else: # position == 'L'
            position -= distance
        # 99/0 circular position correction
        position = abs(position % 100)
        if position == 0:
            password += 1
    print("password:", password)

def main():
    print('\n============================\nAdvent of Code 2025 - Day 1a\n============================\n')
    f = '01.csv'
    #f = '01test.csv'
    sequence = read_input(f) # ['R26', 'L12', 'L47', 'L2', 'R15', ...]
    rotate_dial(sequence)

main()