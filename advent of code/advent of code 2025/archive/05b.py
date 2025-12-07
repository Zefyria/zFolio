# https://adventofcode.com/2025/day/5

'''
So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant.

Test input:
3-5
10-14
16-20
12-18

Test input results:
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20.
So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
'''

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    print('\n============================\nAdvent of Code 2025 - Day 5b\n============================\n')
    f = '05.csv'
    #f = '05test.csv'
    inventory = read_input(f)
    fresh_ranges = []
    answer = 0
    
    for record in inventory:
        if '-' in record:
            minmax = record.split('-')
            fresh_ranges.append([int(minmax[0]),int(minmax[1])]) # stores array [min, max] as integers
    fresh_ranges.sort() # sort by min of ranges
    
    merged = [fresh_ranges[0][:]]
    for start, end in fresh_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    
    for r in merged:
        answer += r[1] - r[0] + 1
    print('number of  ingredient IDs consiered fresh', answer)

main()
