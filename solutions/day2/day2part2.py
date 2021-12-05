FORWARD = "forward"
DOWN = "down"
UP = "up"


def main(input_lines):
    aim = 0
    x = 0
    y = 0
    for line in input_lines:
        split = line.split(" ")
        operation = split[0]
        value = int(split[1])
        if operation == FORWARD:
            x += value
            y += aim * value
        if operation == DOWN:
            aim += value
        if operation == UP:
            aim -= value
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
    assert 900 == main(input_lines)


def test_real_data():
    with open('solutions/day2/input.txt') as f:
        input_lines = f.readlines()
        assert 1960569556 == main(input_lines)
