from utils import timer


file_v = 'text'
file = '2024/Day5/input/' + file_v + '.txt'


@timer
def main():
    rules_list = []
    updates_list = []
    with open(file, 'r') as text:
        for line in text:
            if '|' in line:
                rules_list.append([
                    int(num) for num in line.strip().split('|')])
            if ',' in line:
                updates_list.append([
                    int(num) for num in line.strip().split(',')])

    def fails_test():
        fails_list = []
        for rule in rules_list:
            for update in updates_list:
                if rule[0] in update and rule[1] in update:
                    rule_0_i = update.index(rule[0])
                    rule_1_i = update.index(rule[1])
                    if rule_0_i > rule_1_i and update not in fails_list:
                        fails_list.append(update)
        return fails_list

    def part1():
        part_1_fails = fails_test()
        mid_nums = []
        for update in updates_list:
            if update not in part_1_fails:
                mid_nums.append(update[int((len(update)-1)/2)])
        print(f'part 1 answer: {sum(mid_nums)}')

    def part2():
        part_2_fails = fails_test()

        def fails_fixing(part_2_fails):
            fixes = 0
            for rule in rules_list:
                for fail in part_2_fails:
                    if rule[0] in fail and rule[1] in fail:
                        rule_0_i = fail.index(rule[0])
                        rule_1_i = fail.index(rule[1])
                        if rule_0_i > rule_1_i:
                            fail.pop(rule_0_i)
                            fail.insert(rule_1_i, rule[0])
                            fixes += 1
            return part_2_fails, fixes

        new_fails = fails_fixing(part_2_fails)
        while new_fails[1] > 0:
            new_fails = fails_fixing(new_fails[0])

        mid_nums = []
        for fail in new_fails[0]:
            mid_nums.append(fail[int((len(fail)-1)/2)])
        print(f'part 2 answer: {sum(mid_nums)}')

    part1()
    part2()


main()
