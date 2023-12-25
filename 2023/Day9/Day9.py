import re
from time import time

file_v = 'text'
file = '2023/Day9/input/' + file_v + '.txt'

def timer(func):
    def wrap_function(*args, **kwargs):
        t1 = time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2-t1): .4f}s')
    return wrap_function

@timer
def main():
    histories = []
    with open(file) as data:
        for line in data:
              text = re.findall(r'-?\d+', line)
              ints = [eval(i) for i in text]
              histories.append(ints)
    
    next_values = []
    for history in histories:
        last_sequence_digits = []
        length = len(history)
        last_sequence_digits.append(history[length-1])
        find_differences(history, last_sequence_digits)
        next_value = sum(last_sequence_digits)
        next_values.append(next_value)
    
    sum_next_values = sum(next_values)
    print('Part 1 answer: ' + str(sum_next_values))


def find_differences(sequence, last_sequence_digits):
    length = len(sequence)
    index = 0
    new_level = []
    while index < (length - 1):
        difference = sequence[index+1] - sequence[index]
        new_level.append(difference)
        index += 1
    last_sequence_digits.append(difference)
    if new_level.count(new_level[0]) == len(new_level):
        return difference
    else:
        sequence = new_level
        find_differences(sequence, last_sequence_digits)
    return difference


main()
