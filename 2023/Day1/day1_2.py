num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

file = '2023/Day1/input/text.txt'
with open(file, 'r') as text:
    cal_values = []
    for line in text:
        first_digit = None
        pos = 0
        for char in line:
            if first_digit is None:
                if char.isnumeric():
                    first_digit = char
                    break
                else:
                    for key in num_dict.keys():
                        key_first_letter = key[0]
                        if char == key_first_letter:
                            key_pos = line.find(key)
                            if key_pos == pos:
                                first_digit = num_dict[key]
                                break
                pos = pos + 1
        first_cal_digit = first_digit
        first_digit = None
        last_digit = None
        pos = len(line)
        for char in reversed(line):
            if last_digit is None:
                if char.isnumeric():
                    last_digit = char
                    break
                else:
                    pos = pos - 1
                    for key in num_dict.keys():
                        key_first_letter = key[0]
                        if char == key_first_letter:
                            key_pos = line.rfind(key)
                            if key_pos == pos:
                                last_digit = num_dict[key]
                                break                  
        cal_num = int(first_cal_digit + last_digit)
        print(cal_num)
        cal_values.append(cal_num)
sum_cal_values = sum(cal_values)
print('sum: ' + str(sum_cal_values))