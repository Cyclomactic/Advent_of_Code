import re
from utils import timer


file_v = 'part2_sample'
file = '2023/Day8/input/' + file_v + '.txt'


@timer
def main():
    # read and parse data
    with open(file, 'r') as raw:
        text = raw.readlines()

    lines = []
    for line in text:
        stripped = line.strip('\n')
        lines.append(stripped)
    lines_len = len(lines)
    r_ls = lines[0]

    maps = []
    line_num = 2
    while line_num < lines_len:
        line_clean = re.findall(r'\w{3}', lines[line_num])
        maps.append(line_clean)
        line_num += 1

    # follow maps: part 1
    # start_string = 'AAA'
    # end_string = 'ZZZ'
    # start_tuple = find_index(maps, start_string, location=None)
    # part1 = follow_maps(start_tuple, start_string, r_ls, maps, end_string)
    # print('Part 1 answer: ' + str(part1[0]))

    # follow maps: part 2
    # (\S+Z)
    start_strings = []
    end_strings = []
    # test_strings = []

    for line in lines:
        print(line)
        start_string = re.findall(r'(\S{2}A)', line)
        for string in start_string:
            if start_strings.count(string) == 0:
                start_strings.append(string)
        end_string = re.findall(r'(\S{2}Z)', line)
        for string in end_string:
            if end_strings.count(string) == 0:
                end_strings.append(string)

    for string in start_strings:
        start_tuple = find_index(maps, string, location=None)
        print(start_tuple)
        for e_string in end_strings:
            part2 = follow_maps(start_tuple, string, r_ls, maps, e_string)
            print(part2)


def find_index(maps, string, location):
    if location is None:
        for map in maps:
            if map.count(string) > 0:
                start_index = maps.index(map)
                map_index = map.index(string)
                break
        return start_index, map_index
    else:
        for map in maps:
            if map.count(string) > 0:
                start_index = maps.index(map)
                map_index = map.index(string)
                if map_index != 0:
                    pass
                else:
                    return start_index, map_index


def follow_maps(start_tuple, start_string, r_ls, maps, end_string):
    r_l_index = 0
    r_l_len = len(r_ls)
    start_map = start_tuple[0]
    end_str = start_string
    repititions = 0
    while end_str != end_string:
        for r_l in r_ls:
            r_l_index += 1
            if repititions % 500000 == 0:
                print(repititions)
            if r_l == 'R':
                end_str = maps[start_map][2]
                end_tuple = find_index(maps, end_str, location=(start_map, 2))
            else:
                end_str = maps[start_map][1]
                end_tuple = find_index(maps, end_str, location=(start_map, 1))
            if end_str == end_string:
                repititions += 1
                break
            start_map = end_tuple[0]
            repititions += 1
            if r_l_index == r_l_len:
                r_l_index = 0
    print('repititions = ' + str(repititions))
    return repititions, end_tuple


main()
