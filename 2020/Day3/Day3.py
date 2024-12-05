from utils import timer


file_v = 'text'
file = '2016/Day3/input/' + file_v + '.txt'


@timer
def main():
    with open(file, 'r') as text:
        possible = 0
        for line in text:
            values = line.split()
            values = (list(map(int, values)))
            values.sort()
            if values[0] + values[1] > values[2]:
                possible += 1
    # part 1
    print(f'possible triangles: {possible}')


main()
