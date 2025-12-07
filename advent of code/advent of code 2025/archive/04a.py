# https://adventofcode.com/2025/day/4

'''
The forklifts can only access a roll of paper if there are 
fewer than four rolls of paper in the eight adjacent positions. 
If you can figure out which rolls of paper the forklifts can access, 
they'll spend less time looking and more time breaking down the wall to the cafeteria.

Test input:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Test input results:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
In this example, there are 13 rolls of paper that can be 
accessed by a forklift (marked with x)
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

def check8(grid, row, column):
    count = 0
    for r in range(-1,2):
        for c in range(-1,2):
            try:
                if row-r < 0 or column-c < 0:
                    print('grid edge (< 0)', row-r, column-c)
                elif grid[row-r][column-c] != '.':
                    count += 1
            except IndexError:
                print('grid edge (too large)', row-r, column-c)
            except (ValueError, TypeError) as e:
                print('Error', e)
    # loop runs over itself when r=0 and c=0
    if count - 1 < 4:
        return 'x'
    else:
        return '@'

def main():
    print('\n============================\nAdvent of Code 2025 - Day 4a\n============================\n')
    f = '04.csv' # 137x137
    #f = '04test.csv' # 10x10
    grid = read_input(f)
    #grid = [['@','@','@'],['.','@','.'],['@','@','.']]
    # number of rows (down): len(grid))
    # number of columns (across): len(grid[0])
    answer = 0
    for row in range(0,len(grid)):
        for column in range(0,len(grid[0])):
            if grid[row][column] != '.':
                count = check8(grid, row, column)
                grid[row][column] = count
    for row in range(0,len(grid)):
        for column in range(0,len(grid[0])):
            if grid[row][column] == 'x':
                answer += 1
    print(answer)

main()