import fileinput

instructions = [line for line in fileinput.input()]
# cols   0  1  2
# top = [1, 2, 3] # row 2
# mid = [4, 5, 6] # row 1
# bot = [7, 8, 9] # row 0

keypad = [[7,8,9], [4,5,6], [1,2,3]]

def inc(num):
    return num + 1 if num < 2 else 2

def dec(num):
    return num - 1 if num > 0 else 0

row = 1
col = 1
combo = []

for i in instructions:
    for ch in i:
        if ch == 'U':
            row = inc(row)
        elif ch == 'D':
            row = dec(row)
        elif ch == 'L':
            col = dec(col)
        elif ch == 'R':
            col = inc(col)
        if ch == '\n':
            break
    combo += [keypad[row][col]]

print(combo)
