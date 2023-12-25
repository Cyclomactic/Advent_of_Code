import re 
from time import time
from utils import timer


file_v = 'text'
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

    # follow maps
    r_l_index = 0
    r_l_len = len(r_ls)
    print(r_l_len)
    # (\S{2}+A)
    start_str = 'AAA'
    start_tuple = find_index(maps, start_str, location=None)
    start_map = start_tuple[0]
    end_str = start_str
    repititions = 0
    while end_str != 'ZZZ':
        for r_l in r_ls:
            r_l_index += 1
            if repititions % 500000 == 0:
                print(repititions)
            if r_l == 'R':
                end_str = maps[start_map][2]
                if end_str == 'ZZZ':
                    repititions += 1
                    break
                end_tuple = find_index(maps, end_str, location=(start_map, 2))
                start_map = end_tuple[0]
                repititions += 1
                if r_l_index == r_l_len:
                    r_l_index = 0
            else:
                end_str = maps[start_map][1]
                if end_str == 'ZZZ':
                    repititions += 1
                    break
                end_tuple = find_index(maps, end_str, location=(start_map, 1))
                start_map = end_tuple[0]
                repititions += 1
                if r_l_index == r_l_len:
                    r_l_index = 0
    print('repititions = ' + str(repititions))


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


main()