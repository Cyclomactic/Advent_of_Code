from utils import timer

file_v = 'text'
file = '2024/Day4/input/' + file_v + '.txt'


@timer
def main():
    puzzle = []
    test_list1 = []
    test_list2 = []
    with open(file, 'r') as text:
        for line in text:
            puzzle.append(line)

    def test1(
            puzzle,
            test_list1,
            ln,
            ln2,
            ln3,
            ln4,
            i2,
            i3,
            i4
            ):
        i = 0
        num = 0
        while i < len(puzzle[ln]):
            try:
                if puzzle[ln][i] == 'X':
                    if puzzle[ln+ln2][i+i2] == 'M' and \
                            ln+ln2 >= 0 and \
                            i+i2 >= 0:
                        if puzzle[ln+ln3][i+i3] == 'A' and \
                                ln+ln3 >= 0 and \
                                i+i3 >= 0:
                            if puzzle[ln+ln4][i+i4] == 'S' and \
                                    ln+ln4 >= 0 \
                                    and i+i4 >= 0:
                                x = (ln, i)
                                m = (ln+ln2, i+i2)
                                a = (ln+ln3, i+i3)
                                s = (ln+ln4, i+i4)
                                if (x, m, a, s) not in test_list1:
                                    test_list1.append(puzzle[ln][i])
                                num += 1
                i += 1
            except IndexError:
                i += 1
        return num

    def part1():
        XMAS_num = 0

        def part1_testing(puzzle, test_tuple):
            XMAS_count = 0
            ln = 0
            while ln < len(puzzle):
                XMAS_test = test1(
                    puzzle,
                    test_list1,
                    ln,
                    test_tuple[0],
                    test_tuple[1],
                    test_tuple[2],
                    test_tuple[3],
                    test_tuple[4],
                    test_tuple[5],
                )
                XMAS_count += XMAS_test
                ln += 1
            return XMAS_count

        # forward test XMAS
        forward_tuple = (0, 0, 0, 1, 2, 3)
        forward = part1_testing(puzzle, forward_tuple)
        XMAS_num += forward

        # backward test SAMX
        backward_tuple = (0, 0, 0, -1, -2, -3)
        backward = part1_testing(puzzle, backward_tuple)
        XMAS_num += backward

        # up test
        # S
        # A
        # M
        # X
        up_tuple = (-1, -2, -3, 0, 0, 0)
        up = part1_testing(puzzle, up_tuple)
        XMAS_num += up

        # down test
        # X
        # M
        # A
        # S
        down_tuple = (1, 2, 3, 0, 0, 0)
        down = part1_testing(puzzle, down_tuple)
        XMAS_num += down

        # up_back diagonal test
        # S
        #  A
        #   M
        #    X
        up_back_tuple = (-1, -2, -3, -1, -2, -3)
        up_back = part1_testing(puzzle, up_back_tuple)
        XMAS_num += up_back

        # up_forward diagonal test
        #    S
        #   A
        #  M
        # X
        up_forward_tuple = (-1, -2, -3, 1, 2, 3)
        up_forward = part1_testing(puzzle, up_forward_tuple)
        XMAS_num += up_forward

        # down_back diagonal test
        #    X
        #   M
        #  A
        # S
        down_back_tuple = (1, 2, 3, -1, -2, -3)
        down_back = part1_testing(puzzle, down_back_tuple)
        XMAS_num += down_back

        # down_forward diagonal test
        # X
        #  M
        #   A
        #    S
        down_forward_tuple = (1, 2, 3, 1, 2, 3)
        down_forward = part1_testing(puzzle, down_forward_tuple)
        XMAS_num += down_forward

        return XMAS_num

    def test2(
            puzzle,
            test_list2,
            ln,
            tl,
            tr,
            bl,
            br
            ):
        i = 0
        num = 0
        puzzle_len = len(puzzle)
        line_len = len(puzzle[0])
        while i < len(puzzle[ln]):
            top = ln-1
            left = i-1
            bottom = ln + 1
            right = i + 1
            try:
                if puzzle[ln][i] == 'A':
                    if puzzle[top][left] == tl and \
                            puzzle[bottom][right] == br and \
                            top >= 0 and \
                            left >= 0 and \
                            bottom <= puzzle_len and \
                            right <= line_len:
                        if puzzle[bottom][left] == bl and \
                                puzzle[top][right] == tr and \
                                top >= 0 and \
                                left >= 0 and \
                                bottom <= len(puzzle) and \
                                right <= len(puzzle[0]):
                            topl = (top, left)
                            topr = (top, right)
                            a = (ln, i)
                            botl = (bottom, left)
                            botr = (bottom, right)
                            if (topl, topr, a, botl, botr) not in test_list2:
                                test_list2.append((topl, topr, a, botl, botr))
                            num += 1
                i += 1
            except IndexError:
                i += 1
        return num

    def part2():
        X_MAS_num = 0

        def part2_testing(puzzle, test_str):
            X_MAS_count = 0
            ln = 0
            while ln < len(puzzle):
                X_MAS_test = test2(
                    puzzle,
                    test_list2,
                    ln,
                    test_str[0],
                    test_str[1],
                    test_str[2],
                    test_str[3],
                )
                X_MAS_count += X_MAS_test
                ln += 1
            return X_MAS_count

        #  M S
        #   A
        #  M S
        ms_ms = 'MSMS'
        ms_ms_num = part2_testing(puzzle, ms_ms)
        X_MAS_num += ms_ms_num

        #  S M
        #   A
        #  S M
        sm_sm = 'SMSM'
        sm_sm_num = part2_testing(puzzle, sm_sm)
        X_MAS_num += sm_sm_num

        #  S S
        #   A
        #  M M
        ss_mm = 'SSMM'
        ss_mm_num = part2_testing(puzzle, ss_mm)
        X_MAS_num += ss_mm_num

        #  M M
        #   A
        #  S S
        mm_ss = 'MMSS'
        mm_ss_num = part2_testing(puzzle, mm_ss)
        X_MAS_num += mm_ss_num

        return X_MAS_num

    XMAS_num = part1()
    print(f'XMAS count: {XMAS_num}')

    X_MAS_num = part2()
    print(f'X-MAS count: {X_MAS_num}')


main()
