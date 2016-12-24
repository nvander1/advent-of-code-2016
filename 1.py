directions = input().split(', ')

facing = 'N'
coord = {'x': 0, 'y': 0}

for item in directions:
    turn = item[0]
    dist = int(item[1:])

    if turn == 'L':
        if facing == 'N':
            facing = 'W'
        elif facing == 'E':
            facing = 'N'
        elif facing == 'S':
            facing = 'E'
        else:
            facing = 'S'
    else:
        if facing == 'N':
            facing = 'E'
        elif facing == 'E':
            facing = 'S'
        elif facing == 'S':
            facing = 'W'
        else:
            facing = 'N'

    if facing == 'N':
        coord['y'] += dist
    elif facing == 'E':
        coord['x'] += dist
    elif facing == 'W':
        coord['x'] -= dist
    else:
        coord['y'] -= dist

print('Blocks', abs(coord['x']) + abs(coord['y']))
