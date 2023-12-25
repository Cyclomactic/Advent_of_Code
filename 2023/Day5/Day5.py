import re
from utils import timer


file_v = 'sample'
if file_v == 'sample':
    file = '2023/Day5/input/sample.txt'
else:
    file = '2023/Day5/input/text.txt'

@timer
def main():
    with open(file, 'r') as text:
        blank_lines = []
        seeds_to_soil_map = {}
        soil_to_fert_map = {}
        fert_to_water_map = {}
        water_to_light_map = {}
        light_to_temp_map = {}
        temp_to_humid_map = {}
        humid_to_loc_map = {}
        part_1_locations = []

        whole_text = text.readlines()
        
        for lines in range(len(whole_text)):
            if whole_text[lines] == '\n':
                blank_lines.append(lines)

        # parse data to lists and dictionaries
        seeds_raw = whole_text[0]
        seeds = re.findall(r'[0-9]+', seeds_raw)
        seeds = list(map(int, seeds))

        seeds_to_soil_raw = whole_text[(blank_lines[0]+2):(blank_lines[1])]
        parse_map(seeds_to_soil_raw, seeds_to_soil_map)

        soil_to_fert_raw = whole_text[(blank_lines[1]+2):(blank_lines[2])]
        parse_map(soil_to_fert_raw, soil_to_fert_map)

        fert_to_water_raw = whole_text[(blank_lines[2]+2):(blank_lines[3])]
        parse_map(fert_to_water_raw, fert_to_water_map)

        water_to_light_raw = whole_text[(blank_lines[3]+2):(blank_lines[4])]
        parse_map(water_to_light_raw, water_to_light_map)

        light_to_temp_raw =whole_text[(blank_lines[4]+2):(blank_lines[5])]
        parse_map(light_to_temp_raw, light_to_temp_map)

        temp_to_humid_raw = whole_text[(blank_lines[5]+2):(blank_lines[6])]
        parse_map(temp_to_humid_raw, temp_to_humid_map)

        humid_to_loc_raw = whole_text[(blank_lines[6]+2):len(whole_text)]
        parse_map(humid_to_loc_raw, humid_to_loc_map)

        for seed in seeds:
            seeds_soil = get_directions(seeds_to_soil_map, seed)
            soil_fertilizer = get_directions(soil_to_fert_map, seeds_soil)
            fertilizer_water = get_directions(fert_to_water_map, soil_fertilizer)
            water_light = get_directions(water_to_light_map, fertilizer_water)
            light_temperature = get_directions(light_to_temp_map, water_light)
            temperature_humidity = get_directions(temp_to_humid_map, light_temperature)
            humidity_location = get_directions(humid_to_loc_map, temperature_humidity)
            part_1_locations.append(humidity_location)
        lowest_location_number = min(part_1_locations)
        print('part 1- lowest location number: ' + str(lowest_location_number))

        # part 2 seeds parsing
        part_2_seeds = []
        seeds_len = len(seeds)
        seeds_index = 0
        while seeds_index < seeds_len:
            part_2_seeds.append((seeds[seeds_index], seeds[seeds_index+1]))
            seeds_index += 2
        
        # part 2 
        part_2_locations = 1000000000000
        for item in part_2_seeds:
            print(time())
            seed_start = item[0]
            seeds_range = item[1]
            seed = seed_start
            while seed < seed_start+seeds_range:
                seeds_soil = get_directions(seeds_to_soil_map, seed)
                soil_fertilizer = get_directions(soil_to_fert_map, seeds_soil)
                fertilizer_water = get_directions(fert_to_water_map, soil_fertilizer)
                water_light = get_directions(water_to_light_map, fertilizer_water)
                light_temperature = get_directions(light_to_temp_map, water_light)
                temperature_humidity = get_directions(temp_to_humid_map, light_temperature)
                humidity_location = get_directions(humid_to_loc_map, temperature_humidity)
                if humidity_location < part_2_locations:
                    part_2_locations = humidity_location
                    print(part_2_locations)
                seed += 1
        print(seed)
        print('Part 2- lowest location number: ' + str(part_2_locations))


def get_directions(map_name, seed):
    modded_seed = -1
    for line in map_name:
        destination = map_name[line]['dest']
        source = map_name[line]['source']
        range_len = map_name[line]['range_len']
        if source <= seed < (source+range_len):
            modded_seed = seed-source+destination
    if modded_seed == -1:
        modded_seed = seed
    return modded_seed

def parse_map(raw_map_data, map_name):
    #enumerate()
    dictionary_entry = 0
    for line in raw_map_data:
        data_list = re.findall(r'[0-9]+', line)
        ranges = dict(
            dest=int(data_list[0]),
            source=int(data_list[1]),
            range_len=int(data_list[2]))
        map_name[dictionary_entry] = ranges
        dictionary_entry += 1
    # pprint.pprint(map_name, sort_dicts=False)

main()
