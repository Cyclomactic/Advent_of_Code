from utils import timer, Point


file_v = 'text'
file = '2024/Day6/input/' + file_v + '.txt'

north = Point(0, -1)
east = Point(1, 0)
south = Point(0, 1)
west = Point(-1, 0)

directions = [north, east, south, west]


def parse_data(file):
    with open(file, 'r') as text:
        y = 0
        lines = []
        for line in text:
            lines.append([
                    char for char in line.strip()])
            if '^' in line:
                guard = Point(line.index('^'), y)
            y += 1
    return lines, guard


def move(guard_position, direction):
    possible_position = guard_position + direction
    return possible_position


def cord_check(map, possible_position, dir_index):
    win = False
    can_move_here = True
    len_map = len(map)
    len_line = len(map[0])
    if (
        possible_position.y < 0
        or possible_position.y >= len_map
        or possible_position.x < 0
        or possible_position.x >= len_line
    ):
        win = True
    elif map[possible_position.y][possible_position.x] == '#':
        dir_index += 1
        dir_index = dir_index % len(directions)
        can_move_here = False
    return win, dir_index, can_move_here


def part1(map, guard_position):
    win = False
    can_move_here = True
    unique_positions = set()
    dir_index = 0
    while win is False:
        current_position = guard_position
        if current_position not in unique_positions:
            unique_positions.add(current_position)
        direction = directions[dir_index]
        possible_position = move(guard_position, direction)
        win, dir_index, can_move_here = cord_check(
            map,
            possible_position,
            dir_index
        )
        if can_move_here:
            guard_position = possible_position
    print(f'unique positions: {len(unique_positions)}')


def part2():
    pass


@timer
def main():
    map, guard_position = parse_data(file)

    part1(map, guard_position)
    # print(f'counter: {counter}')
    part2()


main()
