# https://adventofcode.com/2025/day/4

'''
Once a roll of paper can be accessed by a forklift, it can be removed. 
Once a roll of paper is removed, the forklifts might be able to access 
more rolls of paper, which they might also be able to remove. 
How many total rolls of paper could the Elves remove if they keep repeating this process?

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

Test input FINAL ITERATION result:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Stop once no more rolls of paper are accessible by a forklift.
In this example, a total of 43 rolls of paper can be removed.
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
    print('\n============================\nAdvent of Code 2025 - Day 4b\n============================\n')
    f = '04.csv' # 137x137
    #f = '04test.csv' # 10x10
    grid = read_input(f)
    #grid = [['@','@','@'],['.','@','.'],['@','@','.']]
    # number of rows (down): len(grid))
    # number of columns (across): len(grid[0])
    answer = 0
    while True:
        icount = 0
        for row in range(0,len(grid)):
            for column in range(0,len(grid[0])):
                if grid[row][column] != '.':
                    count = check8(grid, row, column)
                    grid[row][column] = count
        for row in range(0,len(grid)):
            for column in range(0,len(grid[0])):
                if grid[row][column] == 'x':
                    icount += 1
                    grid[row][column] = '.' # actually remove roll of paper
        print(icount)
        if icount == 0:
            break
        answer += icount
    print(answer)

main()