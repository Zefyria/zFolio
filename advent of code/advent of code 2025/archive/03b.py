# https://adventofcode.com/2025/day/3

'''
The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; 
the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Test input results:
In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, 
and another 2 battery near the start to produce 434234234278.
In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

987654321111
811111111119
434234234278
888911112111
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def largest(sequence):
    joltage = 0
    for bank in sequence:
        value1 = 0 # value of biggest battery (first digit)
        position1 = 0 # position tracker for value1
        position = 0 # position counter
        for battery in bank[:len(bank)-11]:
            if int(battery) > value1:
                position1 = position
                value1 = int(battery)
            position += 1
        
        value2 = 0 # value of biggest battery after value1 (second digit)
        position2 = position1 + 1 # position tracker for value2
        position = position2 # reset position counter
        for battery in bank[position:-10]:
            if int(battery) > value2:
                position2 = position
                value2 = int(battery)
            position += 1
        
        value3 = 0 # value of biggest battery after value1 (second digit)
        position3 = position2 + 1 # position tracker for value2
        position = position3 # reset position counter
        for battery in bank[position:-9]:
            if int(battery) > value3:
                position3 = position
                value3 = int(battery)
            position += 1
        
        value4 = 0 # value of biggest battery after value1 (second digit)
        position4 = position3 + 1 # position tracker for value2
        position = position4 # reset position counter
        for battery in bank[position:-8]:
            if int(battery) > value4:
                position4 = position
                value4 = int(battery)
            position += 1
        
        value5 = 0 # value of biggest battery after value1 (second digit)
        position5 = position4 + 1 # position tracker for value2
        position = position5 # reset position counter
        for battery in bank[position:-7]:
            if int(battery) > value5:
                position5 = position
                value5 = int(battery)
            position += 1
        
        value6 = 0 # value of biggest battery after value1 (second digit)
        position6 = position5 + 1 # position tracker for value2
        position = position6 # reset position counter
        for battery in bank[position:-6]:
            if int(battery) > value6:
                position6 = position
                value6 = int(battery)
            position += 1
        
        value7 = 0 # value of biggest battery after value1 (second digit)
        position7 = position6 + 1 # position tracker for value2
        position = position7 # reset position counter
        for battery in bank[position:-5]:
            if int(battery) > value7:
                position7 = position
                value7 = int(battery)
            position += 1
        
        value8 = 0 # value of biggest battery after value1 (second digit)
        position8 = position7 + 1 # position tracker for value2
        position = position8 # reset position counter
        for battery in bank[position:-4]:
            if int(battery) > value8:
                position8 = position
                value8 = int(battery)
            position += 1
        
        value9 = 0 # value of biggest battery after value1 (second digit)
        position9 = position8 + 1 # position tracker for value2
        position = position9 # reset position counter
        for battery in bank[position:-3]:
            if int(battery) > value9:
                position9 = position
                value9 = int(battery)
            position += 1

        value10 = 0 # value of biggest battery after value1 (second digit)
        position10 = position9 + 1 # position tracker for value2
        position = position10 # reset position counter
        for battery in bank[position:-2]:
            if int(battery) > value10:
                position10 = position
                value10 = int(battery)
            position += 1

        value11 = 0 # value of biggest battery after value1 (second digit)
        position11 = position10 + 1 # position tracker for value2
        position = position11 # reset position counter
        for battery in bank[position:-1]:
            if int(battery) > value11:
                position11 = position
                value11 = int(battery)
            position += 1

        value12 = 0 # value of biggest battery after value1 (second digit)
        position12 = position11 + 1 # position tracker for value2
        position = position12 # reset position counter
        for battery in bank[position:]:
            if int(battery) > value12:
                position12 = position
                value12 = int(battery)
            position += 1

        #print(bank, '...', value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12)
        joltage += int(str(value1) + str(value2) + str(value3) + str(value4) + str(value5) + str(value6) + str(value7) + str(value8) + str(value9) + str(value10) + str(value11) + str(value12))
    return joltage

def main():
    print('\n============================\nAdvent of Code 2025 - Day 3b\n============================\n')
    f = '03.csv'
    #f = '03test.csv'
    sequence = read_input(f)
    #sequence = ['818181911112111']
    joltage = largest(sequence)
    print(joltage)

main()
