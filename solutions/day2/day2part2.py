import matplotlib.pyplot as plt


FORWARD = "forward"
DOWN = "down"
UP = "up"


def main(input_lines, save_plot=False):
    aim = 0
    x_plots = []
    y_plots = []
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
        y_plots.append(y)
        x_plots.append(x)
    if save_plot:
        # needs graphic capabilities
        plt.plot(x_plots, y_plots)
        plt.xlabel('Distance')
        plt.ylabel('Depth')
        plt.savefig('solutions/day2/part2.png')
    return x_plots[-1] * y_plots[-1]


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
        assert 1960569556 == main(input_lines, save_plot=True)
