from utils import timer


file_v = 'text'
file = '2024/Day1/input/' + file_v + '.txt'


@timer
def main():
    with open(file, 'r') as text:
        splits_1 = []
        splits_2 = []
        for line in text:
            splt_line = line.split()
            splits_1.append(int(splt_line[0]))
            splits_2.append(int(splt_line[1]))
    splits_1.sort()
    splits_2.sort()

    def part1():
        distances = []
        splits_2_index = 0
        for num_A in splits_1:
            if num_A < splits_2[splits_2_index]:
                dist = splits_2[splits_2_index] - num_A
            else:
                dist = num_A - splits_2[splits_2_index]
            distances.append(dist)
            splits_2_index += 1
        total = sum(distances)
        print(f'total distances = {total}')

    part1()

    def part2():
        similarities = []
        for num_A in splits_1:
            multiplier = splits_2.count(num_A)
            sim_score = num_A * multiplier
            similarities.append(sim_score)
        total = sum(similarities)
        print(f'total similarities = {total}')

    part2()


main()
