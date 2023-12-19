from file_utils.read_file import read_file


def get_char_dict(hand):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    char_dict = {}

    for c in hand:
        if c in cards:
            char_dict[c] = char_dict.get(c, 0) + 1

    return char_dict


def card_count_occurrences(hand, count):
    return list(get_char_dict(hand).values()).count(count)


def is_high_card(hand):
    return len(hand) == len(set(hand))


def is_one_pair(hand):
    # 32T3K
    return card_count_occurrences(hand, 2) == 1 and card_count_occurrences(hand, 1) == 3


def is_two_pair(hand):
    # KK677 and KTJJT
    return card_count_occurrences(hand, 2) == 2 and card_count_occurrences(hand, 1) == 1


def is_three_of_kind_pair(hand):
    # T55J5 and QQQJA
    return card_count_occurrences(hand, 3) == 1 and card_count_occurrences(hand, 1) == 2


def is_full_house_pair(hand):
    # 23332
    return card_count_occurrences(hand, 3) == 1 and card_count_occurrences(hand, 2) == 1


def is_four_of_kind_pair(hand):
    # AA8AA
    return card_count_occurrences(hand, 4) == 1 and card_count_occurrences(hand, 1) == 1


def is_five_of_kind_pair(hand):
    # AA8AA
    return card_count_occurrences(hand, 5) == 1


def get_hands_dict(lines):
    hands_dict = {}
    for line in lines:
        hand, bid = line.split()
        hands_dict[hand] = int(bid)

    return hands_dict


def sort_hands(hands_list):
    cards_strength_dict = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4,
                           "3": 3, "2": 2}

    def get_card_strength(card):
        return cards_strength_dict[card]

    def compare_individual_cards(cards1, cards2):
        win_hand = None
        for card1, card2 in zip(cards1, cards2):
            if get_card_strength(card1) == get_card_strength(card2):
                continue
            if get_card_strength(card1) > get_card_strength(card2):
                win_hand = "".join(cards1)
                break
            else:
                win_hand = "".join(cards2)
                break

        return win_hand

    sorted_list = []
    while len(hands_list) > 0:
        if len(hands_list) == 1:
            sorted_list.append(hands_list[0])
            break

        curr = hands_list[0]
        win = curr
        for h in hands_list[1:]:
            win = compare_individual_cards(win, h)
        sorted_list.append(win)
        hands_list.remove(win)

    return sorted_list


def main(hands_list):
    lines = hands_list.splitlines()
    hands_dict = get_hands_dict(lines)

    high_cards = []
    one_pairs = []
    two_pairs = []
    three_of_kind_pairs = []
    full_house_pairs = []
    four_of_kind_pairs = []
    five_of_kind_pairs = []

    hand_categories = [
        ("High Cards", is_high_card, high_cards),
        ("One Pairs", is_one_pair, one_pairs),
        ("Two Pairs", is_two_pair, two_pairs),
        ("Three of a Kind", is_three_of_kind_pair, three_of_kind_pairs),
        ("Full Houses", is_full_house_pair, full_house_pairs),
        ("Four of a Kind", is_four_of_kind_pair, four_of_kind_pairs),
        ("Five of a Kind", is_five_of_kind_pair, five_of_kind_pairs),
    ]

    for category_name, check_function, category_list in hand_categories:
        category_list.extend(hand for hand in hands_dict if check_function(hand))

    ordered = [sort_hands(five_of_kind_pairs), sort_hands(four_of_kind_pairs), sort_hands(full_house_pairs),
               sort_hands(three_of_kind_pairs), sort_hands(two_pairs), sort_hands(one_pairs),
               sort_hands(high_cards)]

    order_of_strength = []
    for sublist in ordered:
        for item in sublist:
            if item:
                order_of_strength.append(item)

    reversed_order_of_strength = order_of_strength[::-1]
    total_win = 0
    for index, element in enumerate(reversed_order_of_strength, 1):
        total_win += hands_dict[element] * index

    return total_win


if __name__ == "__main__":
    hands = read_file("day_07_first_input.txt")
    total_winnings = main(hands)
    print(total_winnings)
