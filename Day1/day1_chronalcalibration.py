def chronal_calibration():
    frequency = 0
    with open("day1_input.txt") as input_file:
        for line in input_file:
            frequency += int(line)
    return frequency


def chronal_calibration_2():
    past_frequencies = set()
    frequency = 0
    while True:
        with open("day1_input.txt") as input_file:
            for line in input_file:
                frequency += int(line)
                if frequency in past_frequencies:
                    return frequency
                past_frequencies.add(frequency)
    return frequency

frequency = chronal_calibration_2()
print frequency, 'is the frequency'