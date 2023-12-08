import re


def main():
    num_letters = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight",
                   "8", "nine", "9"]
    string_to_number = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # num_letters = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight",
    #                "8", "nine", "9"]
    # input = "28gtbkszmrtmnineoneightmx"
    #
    # found_num_letters = []
    # c = ""
    # for char in input:
    #     c += char
    #     print(c)
    #     for n in num_letters:
    #         if c.endswith(n):
    #             found_num_letters.append(n)
    #             c = c[len(n):]  # Remove the matched part from the substring
    #             break
    # print(found_num_letters)

    with open("second_day_input.txt", "r") as file:
        num_sum = 0

        for line in file:
            found_num_letters = []
            c = ""

            for char in line:
                c += char
                for n in num_letters:
                    if n in c:
                        print(f"found it {n}")
                        c = ""
                        found_num_letters.append(n)

            first_num = found_num_letters[0]
            last_num = found_num_letters[-1]

            if not first_num.isdigit():
                first_num = string_to_number.get(first_num)

            if not last_num.isdigit():
                last_num = string_to_number.get(last_num)

            print(first_num, last_num)
            num_sum += int(first_num + last_num)
            print(num_sum)


if __name__ == "__main__":
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
                    last = d
                    if first is None:
                        first = d
            sum += int(first + last)
            print(sum)

