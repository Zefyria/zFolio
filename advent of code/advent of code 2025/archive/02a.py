# https://adventofcode.com/2025/day/1

'''
The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID 
which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), 
and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges.

What do you get if you add up all of the invalid IDs?

Test input results:
11-22                   invalid: 11, 22
95-115                  invalid: 99
998-1012                invalid: 1010
1188511880-1188511890   invalid: 1188511885
222220-222224           invalid: 222222
1698522-1698528
446443-446449           invalid: 446446
38593856-38593862       invalid: 38593859
565653-565659
824824821-824824827
2121212118-2121212124
Adding up all the invalid IDs in this example produces 1227775554.
'''

def read_input(file_path): # need to separate by comma, then by dash
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            parts = cleaned_line.split(',')
    return parts

def test(id):
    validity = True
    # test 1: repeated sequence, eg 55, 6464, 123123
    if len(id) % 2 == 0 and id[0:int(len(id)/2)] == id[int(len(id)/2):]:
        validity = False
        print('id', id, 'repeated sequence')
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
    answer = 0
    for idrange in sequence:
        minmax = idrange.split('-')
        minid = minmax[0]
        maxid = minmax[1]
        for id in range(int(minid), int(maxid)+1):
            answer += test(str(id))
    print(answer)

main()