import re
from functools import reduce
from utils import timer


file_v = 'text'
file = '2023/Day6/input/' + file_v + '.txt'

@timer
def main():
    # Part 1 parse input data
    with open(file, 'r') as text:
        time = text.readline()
        times = re.findall(r'(\d+)', time)
        print(times)
        distance = text.readline()
        distances = re.findall(r'(\d+)', distance)
        print(distances)

    # Part 2 parse input data
    p2_time = time.replace(' ', '')
    p2_times = re.findall(r'(\d+)', p2_time)
    print(p2_times)
    p2_distance = distance.replace(' ', '')
    p2_distances = re.findall(r'(\d+)', p2_distance)
    print(p2_distances)

    # Part 1
    ways_to_beat_record = []  
    races = list(zip(times,distances))
    for race in races:
        race_time = int(race[0])
        record = int(race[1])
        button_press = 0
        distance_traveled = 0
        wins = 0
        while button_press <= race_time:
            run_time = race_time-button_press
            run_distance = button_press*run_time
            if run_distance > record:
                wins +=1
            if run_distance > distance_traveled:
                distance_traveled = run_distance
            button_press += 1
        print('Longest distance traveled: ' + str(distance_traveled))
        print('# of wins: ' + str(wins))
        ways_to_beat_record.append(wins)

    margin_of_error = reduce(lambda x, y: x*y, ways_to_beat_record)
    print('Part 1 answer: ' + str(margin_of_error))

    # Part 2
    ways_to_beat_record = []  
    races = list(zip(p2_times,p2_distances))
    for race in races:
        race_time = int(race[0])
        record = int(race[1])
        button_press = 0
        distance_traveled = 0
        wins = 0
        while button_press <= race_time:
            run_time = race_time-button_press
            run_distance = button_press*run_time
            if run_distance > record:
                wins +=1
            if run_distance > distance_traveled:
                distance_traveled = run_distance
            button_press += 1
        print('Longest distance traveled: ' + str(distance_traveled))
        print('# of wins: ' + str(wins))
        ways_to_beat_record.append(wins)
    print('Part 2 answer: ' + str(ways_to_beat_record))
main()

