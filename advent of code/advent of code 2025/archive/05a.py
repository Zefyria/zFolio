# https://adventofcode.com/2025/day/5

'''
The database operates on ingredient IDs.
- It consists of a list of fresh ingredient ID ranges,
- a blank line, and 
- a list of available ingredient IDs.
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. 
The ranges can also overlap; an ingredient ID is fresh if it is in any range.

How many of the available ingredient IDs are fresh?

Test input:
3-5
10-14
16-20
12-18

1
5
8
11
17
32

Test input results:
Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    print('\n============================\nAdvent of Code 2025 - Day 5a\n============================\n')
    f = '05.csv'
    #f = '05test.csv'
    inventory = read_input(f)
    fresh_ranges = []
    fresh_avail = {}
    answer = 0
    for record in inventory:
        if record == '':
            print('available ingredients ...')
        elif '-' in record:
            minmax = record.split('-')
            fresh_ranges.append(minmax) # stores array [min, max]
        else:
            for i in range(0,len(fresh_ranges)):
                if int(record) >= int(fresh_ranges[i][0]):
                    if int(record) <= int(fresh_ranges[i][1]):
                        fresh_avail[record] = 'fresh'
    for j in fresh_avail:
        answer += 1
    print('number of available ingredient IDs that are fresh', answer)

main()