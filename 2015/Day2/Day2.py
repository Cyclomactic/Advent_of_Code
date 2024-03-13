from utils import timer


file_v = 'sample'
file = '2015/Day2/input/' + file_v + '.txt'


@timer
def main():
    pass


with open(file, 'r') as raw:
    for line in raw:
        clean = line.strip()
        print(clean)

main()
