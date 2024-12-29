from utils import timer


file_v = 'sample2'
file = '2024/Day11/input/' + file_v + '.txt'
multiple = 1


@timer
def main():
    with open(file, 'r') as text:
        for line in text:
            stones = [num for num in line.split()]

    def part1():
        blinks = 0
        while blinks < multiple:
            stone_index = 0
            for stone in stones:
                if stone_index >= len(stones):
                    break
                if stones[stone_index] == '0':
                    stones.pop(stone_index)
                    stones.insert(stone_index, '1')
                    stone_index += 1
                    continue
                if len(stones[stone_index]) % 2 == 0:
                    slice = int(len(stones[stone_index]) / 2)
                    front = stones[stone_index][:slice]
                    back = int(stones[stone_index][slice:])
                    stones.pop(stone_index)
                    stones.insert(stone_index, str(back))
                    stones.insert(stone_index, front)
                    stone_index += 2
                    continue
                else:
                    initial_stone = int(stones[stone_index])
                    stones.pop(stone_index)
                    stones.insert(stone_index, str(initial_stone * 2024))
                    stone_index += 1
            blinks += 1
            print(f'blinks: {blinks}')
            print(f'stones: {stones}')
            print(f'stones len: {len(stones)}')

    def part2(stones):
        blinks = 0
        while blinks < multiple:
            stone_index = 0
            if stone_index >= len(stones):
                break
            stones = [stone if stone != '0' else '1' for stone in stones]
            if len(stones[stone_index]) % 2 == 0:
                slice = int(len(stones[stone_index]) / 2)
                front = stones[stone_index][:slice]
                back = int(stones[stone_index][slice:])
                # stones.pop(stone_index)
                # stones.insert(stone_index, str(back))
                # stones.insert(stone_index, front)
                stones = [
                    x.replace(stones[stone_index],
                              front, back) for x in stones]
                stone_index += 2
                continue
            else:
                initial_stone = int(stones[stone_index])
                stones.pop(stone_index)
                stones.insert(stone_index, str(initial_stone * 2024))
                stones = [
                    x.replace(stones[stone_index],
                              str(initial_stone * 2024)) for x in stones]
                stone_index += 1
            blinks += 1
            print(f'blinks: {blinks}')
            print(f'stones: {stones}')
            print(f'stones len: {len(stones)}')
        pass

    def part3(stones):
        blinks = 0
        while blinks < multiple:
            stone_index = 0
            stone_done = False
            for stone in stones:
                if stone_index >= len(stones):
                    break
                stones = [stone if stone != '0' else '1' for stone in stones]
                if len(stones[stone_index]) % 2 == 0:
                    slice = int(len(stones[stone_index]) / 2)
                    front = stones[stone_index][:slice]
                    back = int(stones[stone_index][slice:])
                    stones.pop(stone_index)
                    stones.insert(stone_index, str(back))
                    stones.insert(stone_index, front)
                    stone_index += 2
                    continue
                initial_stone = int(stones[stone_index])
                stones = [
                    stone if stone_done is False
                    else str(initial_stone * 2024) for stone in stones]
                # else:
                #     initial_stone = int(stones[stone_index])
                #     stones.pop(stone_index)
                #     stones.insert(stone_index, str(initial_stone * 2024))
                stone_index += 1
            blinks += 1
            print(f'blinks: {blinks}')
            print(f'stones: {stones}')
            print(f'stones len: {len(stones)}')
    # part1()
    # part2(stones)
    part3(stones)


main()
