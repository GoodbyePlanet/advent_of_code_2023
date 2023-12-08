from file_utils.read_file import read_file


def main(file):
    num_sum = 0

    for line in file.strip().split("\n"):
        first_num = None
        last_num = None

        for char in line:
            if char.isdigit():
                first_num = char
                break

        for char in line[::-1]:
            if char.isdigit():
                last_num = char
                break

        num_sum += int(first_num + last_num)

    print(f"Sum is: {num_sum}")
    return num_sum


if __name__ == "__main__":
    input_file = read_file("first/first_day_input.txt")
    main(input_file)
