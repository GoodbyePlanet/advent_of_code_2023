def main():
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

    with open("second_day_input.txt", "r") as file:
        for line in file.read().strip().split("\n"):
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
            print(sum)

if __name__ == "__main__":
    main()

