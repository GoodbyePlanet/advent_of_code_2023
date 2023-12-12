from file_utils.read_file import read_file


def main(cards):
    lines = cards.strip().split('\n')

    originals_and_copies = [[] for _ in range(len(lines))]

    for i, line in enumerate(lines):
        numbers = line.split(":")[1].split("|")

        winning_numbers = {int(num) for num in numbers[0].split()}
        my_numbers = {int(num) for num in numbers[1].split()}

        common_numbers = my_numbers.intersection(winning_numbers)
        common_numbers_count = len(common_numbers)

        originals_and_copies[i].append("O")  # add one original card

        for j in range(i + 1, i + common_numbers_count + 1):
            for x in range(len(originals_and_copies[i])):
                originals_and_copies[j].append("C")  # add copy cards

    total_scratchcards = 0

    for c in originals_and_copies:
        total_scratchcards += len(c)

    return total_scratchcards


if __name__ == "__main__":
    colorful_cards = read_file("day_04_second_input.txt")
    result = main(colorful_cards)
    print(result)
