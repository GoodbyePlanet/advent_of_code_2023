from file_utils.read_file import read_file


def all_elements_are_zero(elements):
    return all(element == 0 for element in elements)


def main(report_input):
    lines = report_input.splitlines()

    next_values_of_history = []

    for line in lines:
        values = [int(n) for n in line.split()]
        sequences = [values]

        while not all_elements_are_zero(sequences[-1]):
            next_seq = []
            last_seq = sequences[-1]

            for i in range(len(last_seq) - 1):
                difference = last_seq[i + 1] - last_seq[i]
                next_seq.append(difference)

            sequences.append(next_seq)

        next_value = 0
        for seq in sequences[::-1][1:]:
            next_value = seq[0] - next_value

        next_values_of_history.append(next_value)

    return sum(next_values_of_history)


if __name__ == "__main__":
    report = read_file("day_09_second_input.txt")
    sum_of_extrapolated_values = main(report)
    print(sum_of_extrapolated_values)
