import re


loaded_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
    }

file = '2023/Day2/input/text.txt'
with open(file, 'r') as text:
    possible_games = []
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
        for color in loaded_cubes.keys():
            is_possible = 0
            count = 0
            pos = 0
            while count < names_counts[color]:
                key_pos = line.find(color,pos)
                pos = key_pos + 1
                key_int_index = key_pos - 3
                key_int = line[key_int_index:key_pos-1]
                if int(key_int) <= loaded_cubes.get(color):
                    is_possible = is_possible + 1
                count = count + 1
            if is_possible == names_counts.get(color):
                color_possible = color_possible + 1
        if color_possible == 3:
            possible_games.append(int(game_num))
    total = sum(possible_games)
    print(possible_games)
    print(len(possible_games))
    print('total: ' + str(total))