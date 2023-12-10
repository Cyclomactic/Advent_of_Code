import pprint
import re


sample_numbers = {
    0 : dict(line_num=0, integer=467, start=0, end=3),
    5 : dict(line_num=0, integer= 114, start= 5, end= 8),
    2002 : dict(line_num=2, integer= 35, start= 2, end= 4),
    2006 : dict(line_num=2, integer= 633, start= 6, end= 9),
    4000 : dict(line_num=4, integer= 617, start= 0, end= 3),
    5007 : dict(line_num=5, integer= 58, start= 7, end= 9),
    6002 : dict(line_num=6, integer= 592, start= 2, end= 5),
    7006 : dict(line_num=7, integer= 755, start= 6, end= 9),
    9001 : dict(line_num=9, integer= 664, start= 1, end= 4),
    9005 : dict(line_num=9, integer= 598, start= 5, end= 8),
}

sample_symbols = {
    1003 : dict(line_num=1, symbol='*', position=3),
    3006 : dict(line_num=3, symbol='#', position=6),
    4003 : dict(line_num=4, symbol='*', position=3),
    5005 : dict(line_num=5, symbol='+', position=5),
    8003 : dict(line_num=8, symbol='$', position=3),
    8005 : dict(line_num=8, symbol='*', position=5),
}


def main():
    file = '2023/Day3/input/text.txt'
    with open(file, 'r') as text:
        line_num = 0
        numbers = {}
        symbols = {}
        for line in text:
            num_pos = 0
            sym_pos = 0
            integer_findall = []
            integer_findall = re.findall(r'([^.%+*#@=$&\/\-\s]+)', line)
            if integer_findall != None:
                for integer in integer_findall:
                    num_dict = build_num_dict(integer, line, line_num, num_pos)
                    numbers[key_func(line_num, num_dict['start'])] = num_dict
                    num_pos = num_dict['end']
            symbol_findall = []
            symbol_findall = re.findall(r'([^.0-9\s])', line)
            if symbol_findall != None:
                for symbol in symbol_findall:
                    sym_dict = build_sym_dict(symbol, line, line_num, sym_pos)
                    symbols[key_func(line_num, sym_dict['position'])] = sym_dict
                    sym_pos = sym_dict['position'] + 1
            line_num = line_num + 1 

        # part 1
        part_numbers = []
        p_n = []
        for number in numbers:
            line_number = numbers[number]['line_num']
            index_range_start = numbers[number]['start']
            index_range_end = numbers[number]['end']
            for symbol in symbols:
                check_line = symbols[symbol]['line_num']
                check_pos = symbols[symbol]['position']
                if check_line-1 <= line_number <= check_line+1:
                    if index_range_start-1 <= check_pos <= index_range_end:
                        print(numbers[number]['integer'])
                        part_numbers.append(numbers[number]['integer'])
                        p_n.append(str([numbers[number]['line_num']]) + ' : ' + str( numbers[number]['integer']))
                        pass

        # print(part_numbers)
        print(len(part_numbers))
        Part_numbers_sum = sum(part_numbers)
        print('Part 1- sum of part numbers: ' + str(Part_numbers_sum))

        # Part 2
        gear_ratios = []
        for symbol in symbols:
            if symbols[symbol]['symbol'] == '*':
                check_line = symbols[symbol]['line_num']
                check_pos = symbols[symbol]['position']
                for number in numbers:
                    line_number = numbers[number]['line_num']
                    index_range_start = numbers[number]['start']
                    index_range_end = numbers[number]['end']
                    if check_line-1 <= line_number <= check_line+1:
                        if index_range_start-1 <= check_pos <= index_range_end:
                            first_match = (number, numbers[number]['integer'])
                            for number in numbers:
                                if number != first_match[0]:
                                    line_number = numbers[number]['line_num']
                                    index_range_start = numbers[number]['start']
                                    index_range_end = numbers[number]['end']
                                    if check_line-1 <= line_number <= check_line+1:
                                        if index_range_start-1 <= check_pos <= index_range_end:
                                            second_match = (number, numbers[number]['integer'])
                                            ratio = first_match[1] * second_match[1]
                                            gear_ratios.append(ratio) 
        print(gear_ratios)
        del gear_ratios[1::2]
        print(gear_ratios)
        sum_gears = sum(gear_ratios)
        print('Part 2 answer- sum of gear raitios: ' + str(sum_gears))



def build_num_dict(integer, line, line_num, num_pos):
    position = line.find(integer, num_pos)
    integer_span = len(str(integer))
    integer_start = position
    integer_end = integer_start + integer_span
    num_dict = dict(
        line_num=line_num,
        integer=int(integer),
        start=integer_start,
        end=integer_end,
    )
    return num_dict

def build_sym_dict(symbol, line, line_num, sym_pos):
    position = line.find(symbol, sym_pos)
    sym_dict = dict(
        line_num=line_num,
        symbol=symbol,
        position=position,
    )
    return sym_dict

def key_func(line_num, start):
    key = (line_num * 1000) + start
    return key
main()