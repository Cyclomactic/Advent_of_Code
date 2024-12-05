from utils import timer
import re


file_v = 'text_1'
file = '2024/Day3/input/' + file_v + '.txt'


@timer
def main():
    def parsing(reg_ex):
        with open(file, 'r') as text:
            all = []
            for line in text:
                nums = []
                muls = re.findall(reg_ex, line)
                for string in muls:
                    stripped = string.strip("mul()")
                    converted = stripped.partition(",")
                    x = int(converted[0]) * int(converted[2])
                    nums.append(x)
                p1 = sum(nums)
                all.append(p1)
            all_sum = sum(all)
        return all_sum

    def part1():
        p1_reg_ex = r'(mul\([0-9]+?,[0-9]+?\))'
        sum = parsing(p1_reg_ex)
        print(f'part 1 answer: {sum}')

    def part2():
        # p2_line_reg_ex = r"(do\(\)).*(don't\(\))"
        # with open(file, 'r') as text:
        #     segments = []
        #     for line in text:
        #         seg = re.findall(p2_line_reg_ex, line)
        #         segments.append(seg)
        # p2_reg_ex = r'(mul\([0-9]+?,[0-9]+?\))'
        # all2 = []
        # for line in segments:
        #     nums = []
        #     muls = re.findall(p2_reg_ex, line)
        #     for string in muls:
        #         stripped = string.strip("mul()")
        #         converted = stripped.partition(",")
        #         x = int(converted[0]) * int(converted[2])
        #         nums.append(x)
        #     p1 = sum(nums)
        #     all2.append(p1)
        #     all2_sum = sum(all)
        p2_reg_ex = r'(mul\([0-9]+?,[0-9]+?\))'
        sum = parsing(p2_reg_ex)
        print(f'part 2 answer: {sum}')
        # print(f'part 2 answer: {all2_sum}')

    part1()
    part2()


main()
