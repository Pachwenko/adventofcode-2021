from more_itertools import pairwise


def main(input_lines=None):
    result = 0
    for a, b in pairwise(input_lines):
        if int(a) < int(b):
            result += 1
    return result


def test_example():
    input_lines = [
        "199",
        "200",
        "208",
        "210",
        "200",
        "207",
        "240",
        "269",
        "260",
        "263",
    ]
    assert 7 == main(input_lines)


def test_real_data():
    with open('solutions/day1/input.txt') as f:
        input_lines = f.readlines()
        assert 1266 == main(input_lines)
