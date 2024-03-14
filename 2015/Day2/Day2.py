from utils import timer


file_v = 'text'
file = '2015/Day2/input/' + file_v + '.txt'


@timer
def main():
    pass


with open(file, 'r') as raw:
    total_paper_needed = 0
    total_ribbon_needed = 0
    for line in raw:
        l_w_h = line.split('x')
        l_w_h = (list(map(int, l_w_h)))
        l_w_h.sort()
        top_bot_area = l_w_h[0] * l_w_h[1] * 2
        front_back_area = l_w_h[1] * l_w_h[2] * 2
        side_side_area = l_w_h[2] * l_w_h[0] * 2
        slack = min(top_bot_area, front_back_area, side_side_area)/2
        surface_area = top_bot_area + front_back_area + side_side_area
        paper_needed = surface_area + slack
        total_paper_needed += paper_needed
        top_perimeter = (l_w_h[0] * 2) + (l_w_h[1] * 2)
        volume = l_w_h[0] * l_w_h[1] * l_w_h[2]
        ribbon_needed = top_perimeter + volume
        total_ribbon_needed += ribbon_needed
    # part 1
    print(f'total paper needed: {total_paper_needed}')
    # part 2
    print(f'total ribbon needed: {total_ribbon_needed}')


main()
