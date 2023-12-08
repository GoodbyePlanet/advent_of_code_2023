from file_utils.read_file import read_file


def main(file):
    map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    sum = 0

    for line in file.strip().split("\n"):
        first = None
        second = None
        s = ""
        for char in line:
            d = None
            if char.isdigit():
                d = char
            else:
                s += char
                for k, v in map.items():
                    if s.endswith(k):
                        d = str(v)
            if d is not None:
                second = d
                if first is None:
                    first = d
        sum += int(first + second)

    print(f"Sum is: {sum}")
    return sum


if __name__ == "__main__":
    input_file = read_file("second_day_input.txt")
    main(input_file)
