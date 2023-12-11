import re


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
            winning_nums = set(re.findall(r'([^Card:|\s]+)', line_parts[1]))
            my_nums = set(re.findall(r'([^Card:|\s]+)', line_parts[2]))
            result = winning_nums.intersection(my_nums)
            
            num_points = len(result)
            if num_points != 0:           
                exponent=num_points-1
                base=2
                point_value = 1
                x = point_value*pow(base, exponent)
                points.append(x)

            card_iters = game_nums[str(game_num)]
            while card_iters > 0:
                num = 0
                num_pts = num_points
                while num < num_pts:
                    if num_pts > 0:
                        card_to_add_to = (int(game_num) + num) + 1
                        card_to_add_to_value = game_nums[str(card_to_add_to)]
                        game_nums[str(card_to_add_to)] = card_to_add_to_value + 1
                        num = num + 1
                card_iters = card_iters - 1
            game_num = game_num + 1                    

        part1_total = sum(points)
        print('Part 1 answer = ' + str(part1_total))
        part2_total = sum(game_nums.values())
        print('Part 2 answer = ' + str(part2_total))

def get_game_num(line):
    colon = line.find(':')
    pipe = line.find('|')
    part = line[colon:pipe]
    line_parts = line.partition(part)
    num_search = re.search(r'([^Card:|\s]+)', line_parts[0])
    game_num = num_search.group()
    return game_num

main()
