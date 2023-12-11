from file_utils.read_file import read_file


def main(cards):
    line = cards.strip().split('\n')

    pile_of_scratchcards_worth = 0

    for i in line:
        numbers = i.split(":")[1].split("|")

        winning_numbers = {int(num) for num in numbers[0].split()}
        my_numbers = {int(num) for num in numbers[1].split()}

        common_numbers = my_numbers.intersection(winning_numbers)
        common_numbers_count = len(common_numbers)

        if common_numbers_count > 0:
            pile_of_scratchcards_worth += 2**(common_numbers_count - 1)

    return pile_of_scratchcards_worth


if __name__ == "__main__":
    colorful_cards = read_file("day_04_first_input.txt")
    result = main(colorful_cards)
    print(result)
