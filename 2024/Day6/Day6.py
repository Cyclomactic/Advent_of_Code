from utils import timer, Point


file_v = 'text'
file = '2024/Day6/input/' + file_v + '.txt'

directions = [
    ('north', Point(0, -1)),
    ('east', Point(1, 0)),
    ('south', Point(0, 1)),
    ('west', Point(-1, 0)),
    ]


def parse_data(file):
    with open(file, 'r') as text:
        y = 0
        lines = []
        for line in text:
            lines.append([
                    char for char in line.strip()])
            if '^' in line:
                orig_guard_y = y
                orig_guard_x = line.index('^')
            y += 1
    return lines, orig_guard_x, orig_guard_y


def move(cords, direction):
    new_loc = cords + direction
    return new_loc


def cord_check(map, x, y, index, win=False, check=False):
    len_map = len(map[0])
    len_line = len(map[0][0])
    if y < 0 or y >= len_map or x < 0 or x >= len_line:
        win = True
    elif map[0][y][x] == '#':
        if index == 3:
            index = 0
        else:
            index += 1
        check = True
    return win, index, check


def part1(map):
    win = False
    check = False
    positions = []
    cords = Point(map[1], map[2])
    dir_index = 0
    while win is False:
        position = (cords.x, cords.y)
        if position not in positions:
            positions.append(position)
        direction = directions[dir_index]
        pot_cords = move(cords, direction[1])
        check = cord_check(map, pot_cords.x, pot_cords.y, dir_index)
        win = check[0]
        if check[2] is False:
            cords = pot_cords
        dir_index = check[1]
    print(f'unique positions: {len(positions)}')


def part2():
    pass


@timer
def main():
    map = parse_data(file)

    part1(map)
    part2()


main()
