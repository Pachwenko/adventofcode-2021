import matplotlib.pyplot as plt


ADD_X = "forward"
ADD_Y = "down"  # this is because we are counting "depth"
SUB_Y = "up"


def main(input_lines, save_plot=False):
    x_plots = []
    y_plots = []
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
        y_plots.append(y)
        x_plots.append(x)
    if save_plot:
        # needs graphic capabilities
        plt.plot(x_plots, y_plots)
        plt.xlabel('Distance')
        plt.ylabel('Depth')
        plt.savefig('solutions/day2/part1.png')
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
    assert 150 == main(input_lines)


def test_real_data():
    with open('solutions/day2/input.txt') as f:
        input_lines = f.readlines()
        assert 1813801 == main(input_lines, save_plot=True)
