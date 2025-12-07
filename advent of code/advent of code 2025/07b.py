# https://adventofcode.com/2025/day/7

'''
You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.

Test input:
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............

Test input FINAL results:
.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|
To repair the teleporter, you first need to understand the 
beam-splitting properties of the tachyon manifold. 
In this example, a tachyon beam is split a total of 21 times.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        all = [line.strip() for line in file.readlines()]
        rows = []
        for row in all:
            temp = []
            for char in row:
                temp.append(char)
            rows.append(temp)
        return rows

def find_digit(tachyon, row, column):
    height = len(tachyon)
    digit = 1

    for row in range(row,height):
        if str(tachyon[row][column]).isnumeric() == True:
            digit = tachyon[row][column]
            break
    
    return digit

def main():
    print('\n============================\nAdvent of Code 2025 - Day 7a\n============================\n')
    #f = '07.csv'
    f = '07test.csv'
    tachyon = read_input(f)
    height = len(tachyon)
    width = len(tachyon[0])
    counter = 0

    for row in reversed(range(0,height)):
        for column in range(0,width):
            if tachyon[row][column] == '^':
                left = find_digit(tachyon, row, column-1)
                right = find_digit(tachyon, row, column+1)
                tachyon[row][column] = left + right

    for row in range(0,height):
        for column in range(0,width):
            print(tachyon[row][column], end='')
        print()

    for column in range(0,width):
        if str(tachyon[2][column]).isnumeric() == True:
            print(tachyon[2][column])

main()
