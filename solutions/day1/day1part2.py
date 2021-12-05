from more_itertools import sliding_window


def main(input_lines=None):
    result = 0
    window_size = 4
    for window in sliding_window(input_lines, window_size):
        if window[0] < window[window_size - 1]:
            result += 1
    return result


def test_day1_simple():
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
    assert 5 == main(input_lines)


def test_real_data():
    with open('solutions/day1/input.txt') as f:
        input_lines = f.readlines()
        assert 1217 == main([int(x) for x in input_lines])
