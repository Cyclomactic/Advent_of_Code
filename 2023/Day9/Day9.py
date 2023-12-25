import re
from utils import timer


file_v = 'text'
file = '2023/Day9/input/' + file_v + '.txt'

@timer
def main():
    histories = []
    with open(file) as data:
        for line in data:
              text = re.findall(r'-?\d+', line)
              ints = [int(i) for i in text]
              histories.append(ints)
    
    next_values = []
    first_values = []
    for history in histories:
        last_sequence_digits = []
        first_sequence_digits = []
        length = len(history)
        last_sequence_digits.append(history[length-1])
        find_differences(history, last_sequence_digits, first_sequence_digits)
        next_value = sum(last_sequence_digits)
        next_values.append(next_value)
        # part 2
        first_sequence_digits.append(0)
        len_fsd = len(first_sequence_digits)
        fsd_index = -1
        new_digit_pass = fsd_index
        while (fsd_index*-1) < len_fsd:
            if fsd_index == -1:
                new_digit = first_sequence_digits[fsd_index-1] - first_sequence_digits[fsd_index]
                new_digit_pass = new_digit
                fsd_index -= 1
            else:
                new_digit = first_sequence_digits[fsd_index-1] - new_digit_pass
                new_digit_pass = new_digit
                fsd_index -= 1
        first_values.append(history[0] - new_digit)
    
    sum_next_values = sum(next_values)
    print('Part 1 answer: ' + str(sum_next_values))

    sum_first_values = sum(first_values)
    print('Part 2 answer: ' + str(sum_first_values))

def find_differences(sequence, last_sequence_digits, first_sequence_digits):
    length = len(sequence)
    index = 0
    new_level = []
    while index < (length - 1):
        difference = sequence[index+1] - sequence[index]
        new_level.append(difference)
        index += 1
    last_sequence_digits.append(difference)
    first_sequence_digits.append(new_level[0])
    if new_level.count(new_level[0]) == len(new_level):
        return difference
    else:
        sequence = new_level
        find_differences(sequence, last_sequence_digits, first_sequence_digits)
    return difference


main()
