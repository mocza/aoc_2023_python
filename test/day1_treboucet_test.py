from src import day1_treboucet as t


def test_first_digit():
    assert t.first_digit("1abc2") == "1"
    assert t.first_digit("abc") == ""
    assert t.first_digit("a1bc") == "1"
    assert t.first_digit("abc2") == "2"


def test_last_digit():
    assert t.last_digit("1abc2") == "2"
    assert t.first_digit("abc") == ""
    assert t.first_digit("a1bc") == "1"
    assert t.first_digit("abc2") == "2"


def test_first_and_last_digit_as_number():
    assert t.first_and_last_digit_as_number("abc") == None
    assert t.first_and_last_digit_as_number("1abc") == 11
    assert t.first_and_last_digit_as_number("1abc2") == 12
    assert t.first_and_last_digit_as_number("1ab3c2") == 12


def test_read_file():
    assert "29lzrxseven" in t.read_file(
        "/home/mocha/dev/AoC/2023/python/test/day1_input.txt"
    )


def test_lines_to_numbers():
    assert t.lines_to_numbers(["1abc2"]) == [12]


def test_sum_numbers():
    assert t.sum_numbers([11, 12]) == 23


def test_main():
    assert t.main("/home/mocha/dev/AoC/2023/python/test/day1_input.txt") == 55834
