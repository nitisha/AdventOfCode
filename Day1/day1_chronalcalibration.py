def chronal_calibration():
    frequency = 0

    with open("day1_input.txt") as input_file:
        for line in input_file:
            frequency += int(line)

    return frequency

frequency = chronal_calibration()
print frequency, 'is the frequency'