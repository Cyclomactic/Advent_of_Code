import re
import pprint
from utils import timer


file_v = 'simple_sample'
file = '2023/Day7/input/' + file_v + '.txt'

@timer
def main():
    # parse input file
    hands = []
    lables_1 = [
        ('A', 13),
        ('K', 12),
        ('Q', 11),
        ('J', 10),
        ('T', 9),
        ('9', 8),
        ('8', 7),
        ('7', 6),
        ('6', 5), 
        ('5', 4),
        ('4', 3),
        ('3', 2),
        ('2', 1),
    ]
    lables_2 = [
        ('A', 13),
        ('K', 12),
        ('Q', 11),
        ('T', 10),
        ('9', 9),
        ('8', 8),
        ('7', 7),
        ('6', 6), 
        ('5', 5),
        ('4', 4),
        ('3', 3),
        ('2', 2),
        ('J', 1),
    ]
    with open(file, 'r') as text:
        for line in text:
            raw = line.replace('\n', '').split(' ')
            hands.append(raw)

    # part 1 sort hands
    p1_sorts = sorting(hands, lables_1, 1)
    five_of_a_kind_1 = p1_sorts[0]
    four_of_a_kind_1 = p1_sorts[1]
    full_house_1 = p1_sorts[2]
    three_of_a_kind_1 = p1_sorts[3]
    two_pair_1 = p1_sorts[4]
    one_pair_1 = p1_sorts[5]
    high_card_1 = p1_sorts[6]

    #part 2 sort hands
    p2_sorts = sorting(hands, lables_2, 2)
    five_of_a_kind_2 = p2_sorts[0]
    four_of_a_kind_2 = p2_sorts[1]
    full_house_2 = p2_sorts[2]
    three_of_a_kind_2 = p2_sorts[3]
    two_pair_2 = p2_sorts[4]
    one_pair_2 = p2_sorts[5]
    high_card_2 = p2_sorts[6]
   
    # evaluate hands and rank them
    part_1_evals = evaluating(
        high_card_1,
        one_pair_1,
        two_pair_1,
        three_of_a_kind_1,
        full_house_1,
        four_of_a_kind_1,
        five_of_a_kind_1,
        lables_1,
    )
    part_1_all_hands_ranked = list((part_1_evals))
    part_1_winnings = list((find_winnings(part_1_all_hands_ranked, 1)))
    sum__part_1_winnings = sum(part_1_winnings)
    print('sum part 1 winnings: ' + str(sum__part_1_winnings))

    part_2_evals = evaluating(
        high_card_2,
        one_pair_2,
        two_pair_2,
        three_of_a_kind_2,
        full_house_2,
        four_of_a_kind_2,
        five_of_a_kind_2,
        lables_2,
        )
    part_2_all_hands_ranked = list((part_2_evals))
    pprint.pprint(part_2_all_hands_ranked, sort_dicts=False)
    part_2_winnings = list((find_winnings(part_2_all_hands_ranked, 2)))
    sum__part_2_winnings = sum(part_2_winnings)
    print('sum part 2 winnings: ' + str(sum__part_2_winnings))


def evaluating(
        high_card,
        one_pair,
        two_pair,
        three_of_a_kind,
        full_house,
        four_of_a_kind,
        five_of_a_kind, 
        lables,
    ):
    all_hands_ranked = []
    rank = 0
    high_card_ranked = ordering(high_card, lables, rank)
    # print(high_card_ranked[0])
    rank = high_card_ranked[1]
    all_hands_ranked.extend(high_card_ranked[0])
    print('all hands time: ' + str(time()))

    one_pair_ranked = ordering(one_pair, lables, rank)
    # print(one_pair_ranked[0])
    rank = one_pair_ranked[1]
    all_hands_ranked.extend(one_pair_ranked[0])
    print('one pair time: ' + str(time()))

    two_pair_ranked = ordering(two_pair, lables, rank)
    # print(two_pair_ranked[0])
    rank = two_pair_ranked[1]
    all_hands_ranked.extend(two_pair_ranked[0])
    print('two pair time: ' + str(time()))
    
    three_of_a_kind_ranked = ordering(three_of_a_kind, lables, rank)
    # print(three_of_a_kind_ranked[0])
    rank = three_of_a_kind_ranked[1]
    all_hands_ranked.extend(three_of_a_kind_ranked[0])
    print('three of a kind time: ' + str(time()))
    
    full_house_ranked = ordering(full_house, lables, rank)
    # print(full_house_ranked[0])
    rank = full_house_ranked[1]
    all_hands_ranked.extend(full_house_ranked[0])
    print('full house time: ' + str(time()))
    
    four_of_a_kind_ranked = ordering(four_of_a_kind, lables, rank)
    # print(four_of_a_kind_ranked[0])
    rank = four_of_a_kind_ranked[1]
    all_hands_ranked.extend(four_of_a_kind_ranked[0])
    print('four of a kind time: ' + str(time()))

    
    five_of_a_kind_ranked = ordering(five_of_a_kind, lables, rank)
    # print(five_of_a_kind_ranked[0])
    all_hands_ranked.extend(five_of_a_kind_ranked[0])
    print('five of a kind time: ' + str(time()))
    # high_card = []
    # one_pair = []
    # two_pair = []
    # three_of_a_kind = []
    # full_house = []
    # four_of_a_kind = []
    # five_of_a_kind = []
    return all_hands_ranked


def sorting(hands, lables, part):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    for line in hands:
        hand = line[0]
        if part == 2:
            joker = hand.count('J')
        else:
            joker = 0

        for lable in lables:
            lable_key = lable[0]
            lable_count = hand.count(lable_key)
            if lable_count == 5:
                five_of_a_kind.append(line)
                break
            elif lable_count == 4 and part == 2:
                sorting_4_2(
                    lable_key,
                    line,
                    joker,
                    five_of_a_kind,
                    four_of_a_kind,
                )
                break
            elif lable_count == 4:
                four_of_a_kind.append(line)
                break
            elif lable_count == 3 and part == 2:
                sorting_3_2(
                    lable_key,
                    lables,
                    hand,
                    line,
                    joker,
                    five_of_a_kind,
                    four_of_a_kind,
                    full_house,
                    three_of_a_kind,
                )
                break
            elif lable_count == 3:
                sorting_3(
                    lables,
                    hand,
                    lable_key,
                    line,
                    full_house,
                    three_of_a_kind,
                )
                break
            elif lable_count == 2 and part == 2:
                sorting_2_2(
                    lable_key,
                    lables,
                    hand,
                    line,
                    joker,
                    five_of_a_kind,
                    four_of_a_kind,
                    three_of_a_kind,
                    full_house,
                    two_pair,
                    one_pair,
                )
                break
            elif lable_count == 2:
                sorting_2(
                    lables,
                    hand,
                    lable_key,
                    line,
                    full_house,
                    two_pair,
                    one_pair,
                )
                break
        else:
            if joker == 1:
                one_pair.append(line)
            else:
                high_card.append(line)
    return five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card


def sorting_4_2(
        lable_key,
        line,
        joker,
        five_of_a_kind,
        four_of_a_kind
    ):
    if lable_key == 'J':
        five_of_a_kind.append(line)
        return
    if lable_key != 'J' and joker == 1:
        five_of_a_kind.append(line)
        return
    else:
        four_of_a_kind.append(line)
        return


def sorting_3_2(
        lable_key,
        lables,
        hand,
        line,
        joker,
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
    ):
    if lable_key == 'J':
        for card in lables:
            card_key = card[0]
            card_test = hand.count(card_key)
            if card_test == 2 and card_key != lable_key:
                five_of_a_kind.append(line)
                return
        else:
            four_of_a_kind.append(line)
        return
    if joker == 2:
        five_of_a_kind.append(line)
        return
    elif joker ==1:
        four_of_a_kind.append(line)
        return
    for card in lables:
        card_key = card[0]
        test2 = hand.count(card_key)
        if test2 == 2 and card_key != lable_key:
            full_house.append(line)
            return
    else:
        three_of_a_kind.append(line)
        return


def sorting_3(
        lables,
        hand,
        lable_key,
        line,
        full_house,
        three_of_a_kind,
    ):
    for card in lables:
        card_key = card[0]
        test2 = hand.count(card_key)
        if test2 == 2 and card_key != lable_key:
            full_house.append(line)
            return
    else:
        three_of_a_kind.append(line)
        return


def sorting_2_2(
        lable_key,
        lables,
        hand,
        line,
        joker,
        five_of_a_kind,
        four_of_a_kind,
        three_of_a_kind,
        full_house,
        two_pair,
        one_pair,
    ):
    if lable_key == 'J':
        for card in lables:
            card_key = card[0]
            card_test = hand.count(card_key)
            if card_test == 3 and card_key != lable_key:
                five_of_a_kind.append(line)
                return
            if card_test == 2 and card_key != lable_key:
                four_of_a_kind.append(line)
                return
        else:
            three_of_a_kind.append(line)
            return
    elif joker == 3:
        five_of_a_kind.append(line)
        return
    for item in lables:
        item_key = item[0]
        test3 = hand.count(item_key)
        if test3 == 3 and item != lable_key and joker == 0:
            full_house.append(line)
            return
        elif test3 == 2 and item_key != lable_key:
            if joker == 1:
                full_house.append(line)
                return
            elif joker == 2:
                four_of_a_kind.append(line)
                return
            else:
                two_pair.append(line)
            return
    else:
        if joker == 1:
            three_of_a_kind.append(line)
            return
        else:
            one_pair.append(line)
            return


def sorting_2(
        lables,
        hand,
        lable_key,
        line,
        full_house,
        two_pair,
        one_pair):
    for item in lables:
        item_key = item[0]
        test3 = hand.count(item_key)
        if test3 == 3 and item != lable_key:
            full_house.append(line)
            return
        elif test3 == 2 and item_key != lable_key:
            two_pair.append(line)
            return
    else:
        one_pair.append(line)
        return


def ordering(given_list, lables, rank):
    new_list = []
    if given_list == []:
        return [], rank
    else:
        for hand in given_list:
            new_hand = hand
            character_values = []
            characters = re.findall(r'\w', str(new_hand[0]))
            for character in characters:
                for lable in lables:
                    if character == lable[0]:
                        character_value = int(character.replace(character, str(lable[1])))
                        character_values.append(character_value)
                        break
            new_hand.insert(0, character_values)
            new_list.append(new_hand)
        new_list.sort()
        sorted_list = list(new_list)
        ranked_list = ranking(sorted_list, rank)
        return ranked_list[0], ranked_list[1]


def ranking(sorted_list, rank):
    if rank == 0:
        rank = 1
    for hand in sorted_list:
        hand.insert(0, rank)
        rank += 1
    return sorted_list, rank


def find_winnings(all_hands_ranked, part):
    winnings = []
    for hand in all_hands_ranked:
        if part == 1:
            win = hand[0] * int(hand[3])
        else:
            win = hand[0] * int(hand[3])
        winnings.append(win)
    return winnings


main()