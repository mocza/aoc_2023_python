import re
import sys


def first_digit(string):
    match = re.search(r"^[^\d]*(\d)", string)
    return match.group(1) if match else ""


def last_digit(string):
    match = re.search(r"(\d)[^\d]*$", string)
    return match.group(1) if match else ""


def first_and_last_digit_as_number(string):
    digits = first_digit(string) + last_digit(string)
    return int(digits) if digits != "" else None


def read_file(path):
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


def lines_to_numbers(lines):
    return list(map(lambda s: first_and_last_digit_as_number(s), lines))


def main(path):
    return sum(lines_to_numbers(read_file(path)))


if __name__ == "__main__":
    print(main(sys.argv[1]))
