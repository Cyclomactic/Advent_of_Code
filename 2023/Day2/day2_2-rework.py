import functools
import operator


loaded_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def main():
    file = '2023/Day2/input/text.txt'
    with open(file, 'r') as text:
        powers = []
        for line in text:
            names_counts = {}
            for key in loaded_cubes.keys():
                names_counts[key] = line.count(key)

            maxes = [
                find_color_max("red", names_counts, line),
                find_color_max("green", names_counts, line),
                find_color_max("blue", names_counts, line),
            ]
            
            for color_max in maxes:
                if color_max is None or color_max == 0:
                    maxes.remove(color_max)
            
            power = functools.reduce(operator.mul, maxes, 1)
            powers.append(power)
        powers_sum = sum(powers)
        print('Yo! The answer is ' + str(powers_sum))

def find_color_max(color, names_counts, line):
    color_list = [0]
    count = 0
    pos = 0
    while count < names_counts.get(color):
        color_pos = line.find(color,pos)
        pos = color_pos + 1
        color_int_index = color_pos - 3
        color_int = line[color_int_index:color_pos-1]
        color_list.append(int(color_int))
        count = count + 1
    color_max = max(color_list)
    return color_max
main()