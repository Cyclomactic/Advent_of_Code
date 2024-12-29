from utils import timer


file_v = 'text'
file = '2024/Day11/input/' + file_v + '.txt'
multiple = 25


@timer
def main():
    with open(file, 'r') as text:
        for line in text:
            stones = [num for num in line.split()]

    def part1():
        blinks = 0
        while blinks < multiple:
            stone_index = 0
            while stone_index < len(stones):
                if stones[stone_index] == '0':
                    stones[stone_index] = '1'
                    stone_index += 1
                elif len(stones[stone_index]) % 2 == 0:
                    slice = int(len(stones[stone_index]) / 2)
                    front = stones[stone_index][:slice]
                    back = int(stones[stone_index][slice:])
                    stones[stone_index] = str(back)
                    stones.insert(stone_index, front)
                    stone_index += 2
                else:
                    initial_stone = int(stones[stone_index])
                    stones[stone_index] = str(initial_stone * 2024)
                    stone_index += 1
            blinks += 1
            print(f'stones len: {len(stones)}')

    part1()


main()
