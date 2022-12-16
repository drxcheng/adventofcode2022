SAMPLE = False
Y_TO_TEST = 10 if SAMPLE else 2000000
MAX_X_PART_TWO = 20 if SAMPLE else 4000000
MAX_Y_PART_TWO = 20 if SAMPLE else 4000000

with open(f"dec15{'-sample' if SAMPLE else ''}.txt") as file:
    sensors = []
    beacons = []
    sensor_range = []

    for line in file:
        line = line.rstrip()
        parts = line.split(' ')
        sensor_x = int(parts[2][2:-1])
        sensor_y = int(parts[3][2:-1])
        sensors.append([sensor_x, sensor_y])
        beacon_x = int(parts[8][2:-1])
        beacon_y = int(parts[9][2:])
        if [beacon_x, beacon_y] not in beacons:
            beacons.append([beacon_x, beacon_y])
        sensor_range.append(abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y))

    def find_coverage(x_cover_groups):
        x_coverage = []
        for x_cover in x_cover_groups:
            if len(x_coverage) == 0:
                x_coverage.append([x_cover[0], x_cover[1]])
            else:
                if x_cover[1] <= x_coverage[-1][1]:
                    pass
                elif x_cover[0] <= x_coverage[-1][1] + 1:
                    x_coverage[-1][1] = x_cover[1]
                else:
                    x_coverage.append([x_cover[0], x_cover[1]])
        return x_coverage

    def part_one():
        x_cover_groups = []
        for index, sensor in enumerate(sensors):
            if abs(sensor[1] - Y_TO_TEST) >= sensor_range[index]:
                continue
            x_span = sensor_range[index] - abs(sensor[1] - Y_TO_TEST)
            x_cover_groups.append([sensor[0] - int(x_span), sensor[0] + int(x_span)])

        x_coverage = find_coverage(sorted(x_cover_groups, key=lambda x: x[0]))

        beacon_deduct = 0
        for beacon in beacons:
            if beacon[1] == Y_TO_TEST:
                for x_cover in x_coverage:
                    if beacon[0] >= x_cover[0] and beacon[0] <= x_cover[1]:
                        beacon_deduct += 1
                        break

        x_covered_range = -beacon_deduct
        for x_cover in x_coverage:
            x_covered_range += x_cover[1] - x_cover[0] + 1

        return x_covered_range

    def part_two():
        x_cover_groups_by_y = {}
        for index, sensor in enumerate(sensors):
            for y_to_test in range(max(0, sensor[1] - sensor_range[index]), min(sensor[1] + sensor_range[index], MAX_Y_PART_TWO) + 1):
                if y_to_test not in x_cover_groups_by_y:
                    x_cover_groups_by_y[y_to_test] = []
                x_span = sensor_range[index] - abs(sensor[1] - y_to_test)
                x_cover_groups_by_y[y_to_test].append([sensor[0] - int(x_span), sensor[0] + int(x_span)])

        for y in range(0, MAX_Y_PART_TWO + 1):
            x_coverage = find_coverage(sorted(x_cover_groups_by_y.get(y, []), key=lambda x: x[0]))
            if len(x_coverage) > 1:
                return 4000000 * (x_coverage[0][1] + 1) + y

    print(f'Part One: {part_one()}')
    print(f'Part Two: {part_two()}')
