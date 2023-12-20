from file_utils.read_file import read_file

# mapped to a letters ! < A K Q T, E > D C B !, D > C B !, C > B !
letter_map = {"A": "E", "K": "D", "Q": "C", "T": "B", "J": "!"}


def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def classify(hand):
    curr_score = score(hand)
    jokers = hand.count('J')

    if jokers == 0:
        return curr_score
    for card in hand:
        if card == 'J':
            continue
        t = hand.replace('J', card)
        t_score = score(t)
        if t_score > curr_score:
            curr_score = t_score
    return curr_score


def calculate_strength(hand):
    return classify(hand), [letter_map.get(card, card) for card in hand]


def main(hands_list):
    hands = []
    for line in hands_list.splitlines():
        hand, bid = line.split()
        hands.append((hand, int(bid)))

    hands.sort(key=lambda play: calculate_strength(play[0]))

    winnings = 0

    for rank, (hand, bid) in enumerate(hands, 1):
        winnings += rank * bid

    return winnings


#  Copied from https://www.youtube.com/watch?v=clRDvO3H9fU
if __name__ == "__main__":
    hands_input = read_file("day_07_second_input.txt")
    total_winnings = main(hands_input)
    print(total_winnings)
