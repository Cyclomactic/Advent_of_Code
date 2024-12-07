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

    def test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4):
        i = 0
        num = 0
        while i < len(puzzle[ln]):
            try:
                if puzzle[ln][i] == 'X':
                    if puzzle[ln+ln2][i+i2] == 'M' and ln+ln2 >= 0 and i+i2 >= 0:  # noqa: E501
                        if puzzle[ln+ln3][i+i3] == 'A' and ln+ln3 >= 0 and i+i3 >= 0:  # noqa: E501
                            if puzzle[ln+ln4][i+i4] == 'S' and ln+ln4 >= 0 and i+i4 >= 0:  # noqa: E501
                                x = (ln, i)
                                print(puzzle[ln][i])
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

    def test2(puzzle, test_list2, ln, tl, tr, bl, br):
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
                    if puzzle[top][left] == tl and puzzle[bottom][right] == br and top >= 0 and left >= 0 and bottom <= puzzle_len and right <= line_len:  # noqa: E501
                        if puzzle[bottom][left] == bl and puzzle[top][right] == tr and top >= 0 and left >= 0 and bottom <= len(puzzle) and right <= len(puzzle[0]):  # noqa: E501
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

    def part1():
        XMAS_num = 0

        # forward test XMAS
        ln = 0
        while ln < len(puzzle):
            ln2 = 0
            ln3 = 0
            ln4 = 0
            i2 = 1
            i3 = 2
            i4 = 3
            forward_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += forward_test
            ln += 1

        # backward test SAMX
        ln = 0
        while ln < len(puzzle):
            ln2 = 0
            ln3 = 0
            ln4 = 0
            i2 = -1
            i3 = -2
            i4 = -3
            backward_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += backward_test
            ln += 1

        # up test
        # S
        # A
        # M
        # X
        ln = 0
        while ln < len(puzzle):
            ln2 = -1
            ln3 = -2
            ln4 = -3
            i2 = 0
            i3 = 0
            i4 = 0
            up_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)
            XMAS_num += up_test
            ln += 1

        # down test
        # X
        # M
        # A
        # S
        ln = 0
        while ln < len(puzzle):
            ln2 = 1
            ln3 = 2
            ln4 = 3
            i2 = 0
            i3 = 0
            i4 = 0
            down_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += down_test
            ln += 1

        # up_back diagonal test
        # S
        #  A
        #   M
        #    X
        ln = 0
        while ln < len(puzzle):
            ln2 = -1
            ln3 = -2
            ln4 = -3
            i2 = -1
            i3 = -2
            i4 = -3
            up_back_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += up_back_test
            ln += 1

        # up_forward diagonal test
        #    S
        #   A
        #  M
        # X
        ln = 0
        while ln < len(puzzle):
            ln2 = -1
            ln3 = -2
            ln4 = -3
            i2 = 1
            i3 = 2
            i4 = 3
            up_forward_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += up_forward_test
            ln += 1

        # down_back diagonal test
        #    X
        #   M
        #  A
        # S
        ln = 0
        while ln < len(puzzle):
            ln2 = 1
            ln3 = 2
            ln4 = 3
            i2 = -1
            i3 = -2
            i4 = -3
            down_back_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += down_back_test
            ln += 1

        # down_forward diagonal test
        # X
        #  M
        #   A
        #    S
        ln = 0
        while ln < len(puzzle):
            ln2 = 1
            ln3 = 2
            ln4 = 3
            i2 = 1
            i3 = 2
            i4 = 3
            down_forward_test = test1(puzzle, test_list1, ln, ln2, ln3, ln4, i2, i3, i4)  # noqa: E501
            XMAS_num += down_forward_test
            ln += 1

        return XMAS_num

    def part2():
        X_MAS_num = 0

        # forward x test
        #  M S
        #   A
        #  M S
        ln = 0
        while ln < len(puzzle):
            tl = 'M'
            tr = 'S'
            bl = 'M'
            br = 'S'
            ms_ms_test = test2(puzzle, test_list2, ln, tl, tr, bl, br)
            X_MAS_num += ms_ms_test
            ln += 1

        # backward x test
        #  S M
        #   A
        #  S M
        ln = 0
        while ln < len(puzzle):
            tl = 'S'
            tr = 'M'
            bl = 'S'
            br = 'M'
            sm_sm_test = test2(puzzle, test_list2, ln, tl, tr, bl, br)
            X_MAS_num += sm_sm_test
            ln += 1

        # backward x test
        #  S S
        #   A
        #  M M
        ln = 0
        while ln < len(puzzle):
            tl = 'S'
            tr = 'S'
            bl = 'M'
            br = 'M'
            ss_mm_test = test2(puzzle, test_list2, ln, tl, tr, bl, br)
            X_MAS_num += ss_mm_test
            ln += 1

        # backward x test
        #  M M
        #   A
        #  S S
        ln = 0
        while ln < len(puzzle):
            tl = 'M'
            tr = 'M'
            bl = 'S'
            br = 'S'
            mm_ss_test = test2(puzzle, test_list2, ln, tl, tr, bl, br)
            X_MAS_num += mm_ss_test
            ln += 1
        return X_MAS_num

    XMAS_num = part1()
    print(f'XMAS count: {XMAS_num}')

    X_MAS_num = part2()
    print(f'X-MAS count: {X_MAS_num}')


main()
