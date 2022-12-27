import re
from functools import reduce
from functools import cmp_to_key


class Sensor:
    def distance_to_signal(self, point):
        """
        The Manhattan distance between two points.
        Points are tuples.
        :return: | x1 - x2| + | y1 - y2 |
        """
        return abs(int(point[0]) - int(self.signal[0])) + abs(int(point[1]) - int(self.signal[1]))

    def __init__(self, signal, beacon):
        self.signal = signal
        self.beacon = beacon
        self.distance = self.distance_to_signal(self.beacon)


re_coordinates = re.compile(r'x=(-?\d+), y=(-?\d+)')


def detection_ranges(y, sensors):
    """
    For the given row, calculate the ranges (x1 to x2) of detected beacons
    :param y: the row to calculate
    :param sensors: all the sensors
    :return: An array of tuples. Each tuple is the x1 to x2 range of detections.
    """
    # given a row, find the range (as a tuple) of each sensor's detections
    # start with sensor's distance to beacon, and find delta of y pos of sensor to y pos of target row
    ranges = []
    for sensor in sensors:
        y_diff = abs(y - int(sensor.signal[1]))
        horizontal_diff = sensor.distance - y_diff
        if horizontal_diff >= 0:
            #  reachable
            ranges.append((int(sensor.signal[0]) - horizontal_diff, int(sensor.signal[0]) + horizontal_diff))

    ranges = sorted(ranges, key=cmp_to_key(lambda c1, c2: c1[0] - c2[0]))

    # build a new array of the non overlapping regions.
    horiz_range = ranges[0]
    lower_x = horiz_range[0]
    upper_x = horiz_range[1]
    x_ranges = []
    for i in range(1, len(ranges)):
        horiz_range = ranges[i]

        if horiz_range[0] > upper_x:
            # we're starting a new range
            x_ranges.append((lower_x, upper_x))
            lower_x = horiz_range[0]
            upper_x = horiz_range[1]
            continue

        # if we're here, lower x is within our upper bounds
        upper_x = horiz_range[1] if upper_x < horiz_range[1] else upper_x

    x_ranges.append((lower_x, upper_x))

    return x_ranges


def solve():
    sensors = []
    greatest_distance = 0
    min_x = 0
    max_x = 0
    with open('day15/input.txt', 'r') as file:
        for line in file:
            sensor_coord, beacon_coord = re_coordinates.findall(line)
            sensor = Sensor(sensor_coord, beacon_coord)
            sensors.append(sensor)

            greatest_distance = sensor.distance if sensor.distance > greatest_distance else greatest_distance

            min_x = int(sensor.signal[0]) if int(sensor.signal[0]) < min_x else min_x
            min_x = int(sensor.beacon[0]) if int(sensor.beacon[0]) < min_x else min_x

            max_x = int(sensor.signal[0]) if int(sensor.signal[0]) > max_x else max_x
            max_x = int(sensor.beacon[0]) if int(sensor.beacon[0]) > max_x else max_x

    # part 1
    x_ranges = detection_ranges(2_000_000, sensors)
    detected = reduce(lambda x1, x2: x1 + abs(x2[0] - x2[1]), x_ranges, 0)
    print(f'# detected = {detected}')

    # part 2
    i = 0
    while True:
        # the row with two ranges has a gap of 1 between them, I hope
        detections = detection_ranges(i, sensors)
        if len(detections) == 2:
            x = detections[0][1] + 1
            print(f'x={detections[0][1] + 1}, y={i}')
            print(x * 4_000_000 + i)
            break

        if i == 4_000_000:
            break
        i = i + 1
    exit(1)
