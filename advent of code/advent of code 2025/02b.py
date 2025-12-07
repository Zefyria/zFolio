# https://adventofcode.com/2025/day/1

'''
Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), 
and 1111111 (1 seven times) are all invalid IDs.

Test input results:
11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.
'''

def read_input(file_path): # need to separate by comma, then by dash
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            parts = cleaned_line.split(',')
    return parts

def test(id):
    validity = True
    # test 1: repeated sequence, eg 55, 6464, 123123 -- now also includes 1212121212, 415415415 (repeated 2+ times)
    # longest len(id) = 10 digits
    #         1 digit       2 digit     3 digit     4 digit     5 digit
    # len 2:  11
    # len 3:  111
    # len 4:  1111          1212
    # len 5:  11111
    # len 6:  111111        121212      123123
    # len 7:  1111111
    # len 8:  11111111      12121212                12341234
    # len 9:  111111111                 123123123
    # len 10: 1111111111    1212121212                          1234512345
    if len(id) > 1:
        pattern = id[0]
        if len(id) == 2 and pattern == id[1:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 3 and pattern == id[1:2] and pattern == id[2:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 4 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 5 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:4] and pattern == id[4:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 6 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:4] and pattern == id[4:5] and pattern == id[5:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 7 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:4] and pattern == id[4:5] and pattern == id[5:6] and pattern == id[6:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 8 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:4] and pattern == id[4:5] and pattern == id[5:6] and pattern == id[6:7] and pattern == id[7:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 9 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:4] and pattern == id[4:5] and pattern == id[5:6] and pattern == id[6:7] and pattern == id[7:8] and pattern == id[8:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
        if len(id) == 10 and pattern == id[1:2] and pattern == id[2:3] and pattern == id[3:4] and pattern == id[4:5] and pattern == id[5:6] and pattern == id[6:7] and pattern == id[7:8] and pattern == id[8:9] and pattern == id[9:]:
            validity = False
            print('id', id, 'repeated 1 digit sequence')
    if len(id) % 2 == 0:
        pattern = id[0:2]
        if len(id) == 4 and pattern == id[2:]:
            validity = False
            print('id', id, 'repeated 2 digit sequence')
        if len(id) == 6 and pattern == id[2:4] and pattern == id[4:]:
            validity = False
            print('id', id, 'repeated 2 digit sequence')
        if len(id) == 8 and pattern == id[2:4] and pattern == id[4:6] and pattern == id[6:]:
            validity = False
            print('id', id, 'repeated 2 digit sequence')
        if len(id) == 10 and pattern == id[2:4] and pattern == id[4:6] and pattern == id[6:8] and pattern == id[8:]:
            validity = False
            print('id', id, 'repeated 2 digit sequence')
    if len(id) % 3 == 0:
        pattern = id[0:3]
        if len(id) == 6 and pattern == id[3:]:
            validity = False
            print('id', id, 'repeated 3 digit sequence')
        if len(id) == 9 and pattern == id[3:6] and pattern == id[6:]:
            validity = False
            print('id', id, 'repeated 3 digit sequence')
    if len(id) % 4 == 0:
        pattern = id[0:4]
        if len(id) == 8 and pattern == id[4:]:
            validity = False
            print('id', id, 'repeated 4 digit sequence')
    if len(id) % 5 == 0:
        pattern = id[0:5]
        if len(id) == 10 and pattern == id[5:]:
            validity = False
            print('id', id, 'repeated 5 digit sequence')
    # test 2: leading zero, eg 0101
    if id[0] == '0':
        validity = False
        print('id', id, 'leading zero')
    # if invalid, return id, else 0
    if validity == True:
        return 0
    else:
        return int(id)

def main():
    print('\n============================\nAdvent of Code 2025 - Day 2a\n============================\n')
    f = '02.csv'
    #f = '02test.csv'
    sequence = read_input(f)
    #sequence = ['9-13']
    answer = 0
    for idrange in sequence:
        minmax = idrange.split('-')
        minid = minmax[0]
        maxid = minmax[1]
        for id in range(int(minid), int(maxid)+1):
            answer += test(str(id))
    print(answer)

main()