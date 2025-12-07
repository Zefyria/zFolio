# https://adventofcode.com/2025/day/6

'''
The math worksheet (your puzzle input) consists of a list of problems; 
each problem has a group of numbers that need to either be 
either added (+) or multiplied (*) together.

Test input:
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Test input results:
this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total 
of adding together all of the answers to the individual problems. 
In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        all = [line.strip() for line in file.readlines()]
        rows = []
        for row in all:
            temp = []
            for i in row.split(' '):
                if i != '':
                    temp.append(i)
            rows.append(temp)
        return rows

def split_worksheet(worksheet):
    multiply = []
    add = []
    
    for column in range(0,len(worksheet[0])):
        problem = []
        for row in range(0,len(worksheet)):
            problem.append(worksheet[row][column])
        if problem[-1] == '*':
            multiply.append(problem[0:-1])
        else:
            add.append(problem[0:-1])
    return multiply, add

def main():
    print('\n============================\nAdvent of Code 2025 - Day 6a\n============================\n')
    f = '06.csv'
    #f = '06test.csv'
    worksheet = read_input(f)
    
    multiply, add = split_worksheet(worksheet)

    answer = 0
    for problem in multiply:
        temp = 1
        for i in problem:
            temp *= int(i)
        answer += temp
    for problem in add:
        temp = 0
        for i in problem:
            temp += int(i)
        answer += temp
    print(answer)
    
main()