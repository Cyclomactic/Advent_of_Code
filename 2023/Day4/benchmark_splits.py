import re
from typing import List
# from utils import load_input


def load_input(year: int, day: int) -> List[str]:
    with open('2023/Day4/input/text.txt') as file:
        return list(file)


lines = load_input(2023, 4)


def cyclo():
    data = []
    for line in lines:
        colon = line.find(':')
        pipe = line.find('|')
        part = line[colon:pipe]
        line_parts = line.partition(part)
        winning_nums = set(int(x) for x in re.findall(r'[0-9]+', line_parts[1]))  # noqa: E501
        my_nums = set(int(x) for x in re.findall(r'[0-9]+', line_parts[2]))
        data.append((winning_nums, my_nums))
    return data


def kozzi_full_regex():
    data = []
    for line in lines:
        if line == '':
            continue
        parts = re.split(':|\\|', line)
        winning_nums = set(int(x) for x in re.findall('[0-9]+', parts[1]))
        my_nums = set(int(x) for x in re.findall('[0-9]+', parts[2]))
        data.append((winning_nums, my_nums))
    return data


def kozzi_minimal_regex():
    data = []
    for line in lines:
        if line == '':
            continue
        parts = re.split(':|\\|', line)
        winning_nums = set(int(num) for num in parts[1].strip().split(' ') if num != '')  # noqa: E501
        my_nums = set(int(num) for num in parts[2].strip().split(' ') if num != '')  # noqa: E501
        data.append((winning_nums, my_nums))
    return data


def kozzi_no_regex():
    data = []
    for line in lines:
        if line == '':
            continue
        colon = line.find(':')
        pipe = line.find('|')
        part1 = line[colon+1:pipe]
        part2 = line[pipe+1:]
        winning_nums = set(int(num) for num in part1.strip().split(' ') if num != '')  # noqa: E501
        my_nums = set(int(num) for num in part2.strip().split(' ') if num != '')  # noqa: E501
        data.append((winning_nums, my_nums))
    return data


def kozzi_manual():
    data = []
    for line in lines:
        if line == '':
            continue

        colon_reached = False
        pipe_reached = False
        winning_nums = set()
        my_nums = set()
        tmp_num = ''

        for c in line:
            if not colon_reached and c == ':':
                colon_reached = True
                tmp_num = ''
            elif not pipe_reached and c == '|':
                pipe_reached = True
                tmp_num = ''
            elif c.isdigit():
                tmp_num += c
            elif c == ' ':
                if tmp_num != '':
                    tmp_num = int(tmp_num)
                    if pipe_reached:
                        my_nums.add(tmp_num)
                    elif colon_reached:
                        winning_nums.add(tmp_num)
                tmp_num = ''

        if tmp_num != '':
            tmp_num = int(tmp_num)
            my_nums.add(tmp_num)

        data.append((winning_nums, my_nums))

    return data


if __name__ == '__main__':
    c = cyclo()
    k1 = kozzi_full_regex()
    k2 = kozzi_minimal_regex()
    k3 = kozzi_no_regex()
    k4 = kozzi_manual()

    print(str(c == k1))
    print(str(c == k2))
    print(str(c == k3))
    print(str(c == k4))

    # print(str(c[1]))
    # print(str(k4[1]))

    import timeit
    iterations = 1000
    functions = [
        'cyclo',
        'kozzi_full_regex',
        'kozzi_minimal_regex',
        'kozzi_no_regex',
        'kozzi_manual',
    ]

    for function_name in functions:
        print('{:30s} = {:.6f} s'.format(
            function_name,
            timeit.timeit(function_name + '()', globals=locals(), number=iterations)  # noqa: E501
        ))
