from collections import Counter


def most_common(items):
    return Counter(items).most_common()[0][0]


def least_common(items):
    return Counter(items).most_common()[-1][0]


def main(input_lines):
    gamma = ""
    epsilon = ""
    for x in range(len(input_lines[0])):
        column = [y[x] for y in input_lines]
        gamma += most_common(column)
        epsilon += least_common(column)
    return int(gamma, 2) * int(epsilon, 2)


def test_example():
    input_lines = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    assert 198 == main(input_lines)


def test_real_data():
    with open('solutions/day3/input.txt') as f:
        input_lines = f.readlines()
        assert 2595824 == main(input_lines)
