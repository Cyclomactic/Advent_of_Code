import re
import time


file_v = 'text'
if file_v == 'sample':
    file = '2023/Day4/input/sample.txt' 
else:
    file = '2023/Day4/input/text.txt'

def main():
    with open(file, 'r') as text:
        game_nums = {}
        for line in text:
            game_num = get_game_num(line)
            game_nums[game_num] = 1

    with open(file, 'r') as text:
        points = []
        game_num = 1
        for line in text:
            colon = line.find(':')
            pipe = line.find('|')
            part = line[colon:pipe]
            line_parts = line.partition(part)
            winning_nums = set(re.findall(r'[0-9]+', line_parts[1]))
            my_nums = set(re.findall(r'[0-9]+', line_parts[2]))
            result = winning_nums.intersection(my_nums)
            
            num_points = len(result)
            if num_points != 0:           
                exponent=num_points-1
                base=2
                point_value = 1
                x = point_value*pow(base, exponent)
                points.append(x)

            num = 0
            num_pts = num_points
            while num < num_pts:
                card_to_add_to = (game_num + num) + 1
                card_iters = game_nums[game_num]
                game_nums[card_to_add_to] += card_iters
                num += 1
            game_num += 1     

        part1_total = sum(points)
        print('Part 1 answer = ' + str(part1_total))
        part2_total = sum(game_nums.values())
        print('Part 2 answer = ' + str(part2_total))

def get_game_num(line):
    colon = line.find(':')
    pipe = line.find('|')
    part = line[colon:pipe]
    line_parts = line.partition(part)
    num_search = re.search(r'[0-9]+', line_parts[0])
    game_num = int(num_search.group())
    return game_num

start = time.time()

main()

taken = time.time() - start
print(taken)