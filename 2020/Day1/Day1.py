from utils import timer


file_v = 'text'
file = '2020/Day1/input/' + file_v + '.txt'


@timer
def main():
    with open(file, 'r') as text:
        my_list = []
        for number_one in text:
            print(f'number 1: {number_one}')
            clean_1 = number_one.strip()
            my_list.append(clean_1)
        print(my_list)
        for item in my_list:
            number_2 = str(2020 - int(item))
            try:
                if number_2 in my_list:
                    print(f'here it is: {number_2}')
                    print(f'number 1: {item}')
                    print(f'Part 1 answer: {int(item)*int(number_2)}')
            except Exception:
                print("not yet")


main()
