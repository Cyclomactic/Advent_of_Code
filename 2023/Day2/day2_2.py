import re
import functools
import operator


loaded_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
    }


file = '2023/Day2/input/text.txt'
with open(file, 'r') as text:
    powers = []
    for line in text:
        color_possible = 0
        game = re.search(r'[0-9]+', line)
        game_num = game.group()
        names = []
        counts = []
        for key in loaded_cubes.keys():
            key_count = line.count(key)
            names.append(key)
            counts.append(key_count)
        names_counts = {}
        for name in names:
            for count in counts:
                names_counts[name] = count
                counts.remove(count)
                break

        maxes = []

        red_list = [0]
        count = 0
        pos = 0
        while count < names_counts.get('red'):
            color_pos = line.find('red',pos)
            pos = color_pos + 1
            color_int_index = color_pos - 3
            color_int = line[color_int_index:color_pos-1]
            red_list.append(int(color_int))
            count = count + 1
        red_max = max(red_list)
        if red_max > 0:
                maxes.append(red_max)
        

        green_list = [0]
        count = 0
        pos = 0
        while count < names_counts.get('green'):
            color_pos = line.find('green',pos)
            pos = color_pos + 1
            color_int_index = color_pos - 3
            color_int = line[color_int_index:color_pos-1]
            green_list.append(int(color_int))
            count = count + 1
        green_max = max(green_list)
        if green_max > 0:
                maxes.append(green_max)


        blue_list = [0]
        count = 0
        pos = 0
        while count < names_counts.get('blue'):
            color_pos = line.find('blue',pos)
            pos = color_pos + 1
            color_int_index = color_pos - 3
            color_int = line[color_int_index:color_pos-1]
            blue_list.append(int(color_int))
            count = count + 1
        blue_max = max(blue_list)
        if blue_max > 0:
                maxes.append(blue_max)

        power = functools.reduce(operator.mul, maxes, 1)
        powers.append(power)
    powers_sum = sum(powers)
    print('Yo! The answer is ' + str(powers_sum))