ADD_X = "forward"
ADD_Y = "down"  # this is because we are counting "depth"
SUB_Y = "up"


def main(input_lines):
    x = 0
    y = 0
    for line in input_lines:
        split = line.split(" ")
        operation = split[0]
        value = int(split[1])
        if operation == ADD_X:
            x += value
        if operation == ADD_Y:
            y += value
        if operation == SUB_Y:
            y -= value
    return x * y


def test_example():
    input_lines = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    assert 150 == main(input_lines)


def test_real_data():
    with open('solutions/day2/input.txt') as f:
        input_lines = f.readlines()
        assert 1813801 == main(input_lines)
