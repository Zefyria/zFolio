# https://adventofcode.com/2025/day/6

'''
Cephalopod math is written right-to-left in columns. 
Each number is given in its own column, 
with the most significant digit at the top 
and the least significant digit at the bottom. 
(Problems are still separated with a column consisting only of spaces, 
and the symbol at the bottom of the problem is still the operator to use.)

Test input:
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Test input results:
Reading the problems right-to-left one column at a time, the problems are now quite different:
The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        all = [line.rstrip("\n") for line in file.readlines()]
        rows = []
        for row in all:
            temp = []
            for char in row:
                temp.append(char)
            rows.append(temp)
        return rows

def main():
    print('\n============================\nAdvent of Code 2025 - Day 6b\n============================\n')
    f = '06.csv'
    #f = '06test.csv'
    worksheet = read_input(f)

    operation = []

    for i in reversed(range(0,len(worksheet[-1]))):
        if worksheet[-1][i] != ' ':
            operation.append(worksheet[-1][i])

    number = []
    problem = []

    for column in reversed(range(0,len(worksheet[0]))):
        num = ''
        for row in range(0,len(worksheet)-1):
            if worksheet[row][column] != ' ':
                num += worksheet[row][column]
        if num == '' or column == len(worksheet[0]):
            number.append(problem)
            problem = []
        else:
            problem.append(num)
    
    number.append(problem)

    answer = 0

    for i in range(0,len(operation)):
        if operation[i] == '+':
            temp = 0
        else:
            temp = 1
        for j in range(0,len(number[i])):
            if operation[i] == '+':
                temp += int(number[i][j])
            else:
                temp *= int(number[i][j])
        answer += temp
    
    print(answer)
    
main()