SAMPLE = False
Y_TO_TEST = 10 if SAMPLE else 2000000
MAX_X_PART_TWO = 20 if SAMPLE else 4000000
MAX_Y_PART_TWO = 20 if SAMPLE else 4000000

with open(f"dec15{'-sample' if SAMPLE else ''}.txt") as file:
    sensors = []
    beacons = []
    sensor_closest_distance = []
    min_x = None
    max_x = None
    min_y = None
    max_y = None

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
        sensor_closest_distance.append(abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y))

        if min_x is None or min(sensor_x, beacon_x) < min_x:
            min_x = min(sensor_x, beacon_x)
        if max_x is None or max(sensor_x, beacon_x) > max_x:
            max_x = max(sensor_x, beacon_x)
        if min_y is None or min(sensor_y, beacon_y) < min_y:
            min_y = min(sensor_y, beacon_y)
        if max_y is None or max(sensor_y, beacon_y) > max_y:
            max_y = max(sensor_y, beacon_y)

    def can_place_beacon(x, y):
        for index, sensor in enumerate(sensors):
            distance = abs(sensor[0] - x) + abs(sensor[1] - y)
            if distance <= sensor_closest_distance[index]:
                return False
        return True

    no_of_positions = 0
    to_extend_min = False
    to_extend_max = False
    for x in range(min_x, max_x + 1):
        if [x, Y_TO_TEST] in beacons:
            continue

        if not can_place_beacon(x, Y_TO_TEST):
            no_of_positions += 1
            if x == min_x:
                to_extend_min = True
            if x == max_x:
                to_extend_max = True

    if to_extend_min:
        x = min_x - 1
        while not can_place_beacon(x, Y_TO_TEST):
            no_of_positions += 1
            x -= 1
    if to_extend_max:
        x = max_x + 1
        while not can_place_beacon(x, Y_TO_TEST):
            no_of_positions += 1
            x += 1

    print(f'Part One: {no_of_positions}')

    found_beacon = False
    for x in range(0, MAX_X_PART_TWO + 1):
        print(x)
        for y in range(0, MAX_Y_PART_TWO + 1):
            if can_place_beacon(x, y):
                found_beacon = True
                # print(f'found position ({x}, {y})')
                break
        if found_beacon:
            break

    print(f'found position ({x}, {y})')
    print(f'Part Two: {x * 4000000 + y}')
