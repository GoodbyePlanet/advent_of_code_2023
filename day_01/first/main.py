def main():
    with open("first/first_day_input.txt", "r") as file:
        num_sum = 0

        for line in file:
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

        print(type(first_num), type(last_num), num_sum)


if __name__ == "__main__":
    main()
