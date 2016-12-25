from sys import stdin

def rect(m, n, s):
    for col in range(m):
        for row in range(n):
            s[row][col] = '#'

def rotate_row(n, row, s):
    if n == 0:
        return
    init = s[row][:-1]
    last = list(s[row][-1])
    s[row] = last+init
    rotate_row(n-1, row, s)

def rotate_col(n, col, s):
    temp = transpose(s)
    rotate_row(n, col, temp)
    s.clear()
    s += transpose(temp)

def transpose(s):
    return list(map(list, zip(*s)))

screen = [['.'] * 50 for _ in range(6)]
for line in stdin.readlines():
    if 'rect' in line:
        temp = line[5:-1].split('x')
        rect(int(temp[0]), int(temp[1]), screen)
    elif 'column' in line:
        temp = [int(s) for s in line[16:-1].split(' by ')]
        rotate_col(temp[1], temp[0], screen)
    else:
        temp = [int(s) for s in line[13:-1].split(' by ')]
        rotate_row(temp[1], temp[0], screen)
print(''.join([''.join(row) for row in screen]).count('#'))
