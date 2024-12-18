import re
from utils import timer


file_v = 'text'
file = '2023/Day11/input/' + file_v + '.txt'


@timer
def main():
    with open(file) as raw:
        text = raw.readlines()

    lines = []
    for line in text:
        stripped = line.strip('\n')
        lines.append(stripped)

    # find galaxies
    galaxies = []
    for row_index, row in enumerate(lines, 0):
        row_len = len(row)
        col_index = 0
        while col_index < row_len:
            galaxy = row.find('#', col_index)
            if galaxy >= 0:
                col_index = galaxy + 1
            else:
                break
            galaxies.append((row_index, galaxy))
    len_g = len(galaxies)
    print('number of galaxies: ' + str(len_g))

    # find empty rows and columns
    empty_rows = []
    for index, row in enumerate(lines, 0):
        has_galaxy = re.search(r'#', row)
        if has_galaxy is None:
            empty_rows.append(index)

    empty_columns = []
    column_test = []
    x = 0
    while x < len(lines[0]):
        for line in lines:
            test(line, x, column_test)
            if column_test == []:
                x += 1
                break
        if len(column_test) == len(lines):
            empty_columns.append(x)
            x += 1
            column_test = []
    print('empty_row: ' + str(empty_rows))
    print('empty_column: ' + str(empty_columns))

    # measure between galaxies
    # part 1
    paths = 0
    for start_galaxy, start_location in enumerate(galaxies, 0):
        path = measuring(galaxies, start_galaxy, start_location, empty_columns, empty_rows, 1)  # noqa: E501
        paths += path
    print('Part 1 answer: ' + str(paths))

    # part 2
    paths = 0
    for start_galaxy, start_location in enumerate(galaxies, 0):
        path = measuring(galaxies, start_galaxy, start_location, empty_columns, empty_rows, 999999)  # noqa: E501
        paths += path
    print('Part 2 answer: ' + str(paths))


def measuring(galaxies, start_galaxy, start_location, empty_columns, empty_rows, multiplier):  # noqa: E501
    distances = 0
    for galaxy, location in enumerate(galaxies, 0):
        distance = 0
        if start_galaxy < galaxy:
            row_to_sub_from = location[0]
            row_distance = row_to_sub_from - start_location[0]
            add_distance = 0
            for row in empty_rows:
                if start_location[0] < row < row_to_sub_from or start_location[0] > row > row_to_sub_from:  # noqa: E501
                    add_distance += multiplier
            col_to_sub_from = location[1]
            col_distance = col_to_sub_from - start_location[1]
            for col in empty_columns:
                if start_location[1] < col < col_to_sub_from or start_location[1] > col > col_to_sub_from:  # noqa: E501
                    add_distance += multiplier
            distance = abs(col_distance) + abs(row_distance) + add_distance
            distances += distance
    return distances


def test(line, x, column_test):
    if line[x] == '#':
        column_test.clear()
    else:
        column_test.append(x)


main()
