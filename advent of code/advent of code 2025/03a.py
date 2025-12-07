# https://adventofcode.com/2025/day/3

'''
The batteries are arranged into banks; each line of digits in your input 
corresponds to a single bank of batteries. Within each bank, you need to 
turn on exactly two batteries; the joltage that the bank produces is 
equal to the number formed by the digits on the batteries you've turned on. 
For example, if you have a bank like 12345 and you turn on batteries 2 and 4, 
the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce.

Test input results:
In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
In 818181911112111, the largest joltage you can produce is 92.
The total output joltage is the sum of the maximum joltage from each bank, 
so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def largest(sequence):
    # first digit = largest battery (exclude last battery)
    # work with positions in array, not digits, to translate lookup
    # second digit = largest battery after first digit
    joltage = 0
    for bank in sequence:
        value1 = 0 # value of biggest battery (first digit)
        position1 = 0 # position tracker for value1
        position = 0 # position counter
        for battery in bank[:len(bank)-1]:
            if int(battery) > value1:
                position1 = position
                value1 = int(battery)
            position += 1
        value2 = 0 # value of biggest battery after value1 (second digit)
        position2 = position1 + 1 # position tracker for value2
        position = 0 # reset position counter
        for battery in bank[position2:]:
            if int(battery) > value2:
                position2 = position
                value2 = int(battery)
            position += 1
        joltage += int(str(value1) + str(value2))
    return joltage

def main():
    print('\n============================\nAdvent of Code 2025 - Day 3a\n============================\n')
    f = '03.csv'
    #f = '03test.csv'
    sequence = read_input(f)
    joltage = largest(sequence)
    print(joltage)

main()


