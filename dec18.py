import functools

SAMPLE = True

with open(f"dec18{'-sample' if SAMPLE else ''}.txt") as file:
    cubes = []

    min_x = None
    max_x = None
    min_y = None
    max_y = None
    min_z = None
    max_z = None

    for line in file:
        [x, y, z] = list(map(int, line.rstrip().split(',')))
        if min_x is None or x < min_x:
            min_x = x
        if max_x is None or x > max_x:
            max_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_y is None or y > max_y:
            max_y = y
        if min_z is None or z < min_z:
            min_z = z
        if max_z is None or z > max_z:
            max_z = z
        cubes.append([x, y, z])

    def getTotalSurfaces(surfaces):
        total_surfaces = 6 * len(surfaces)
        for [x1, y1, z1] in surfaces:
            for [x2, y2, z2] in surfaces:
                if ([x1, y1] == [x2, y2] and abs(z1 - z2) == 1) \
                    or ([x1, z1] == [x2, z2] and abs(y1 - y2) == 1) \
                    or ([y1, z1] == [y2, z2] and abs(x1 - x2) == 1):
                    total_surfaces -= 1
        return total_surfaces

    part_one_result = getTotalSurfaces(cubes)
    print(f'Part One: {part_one_result}')

    exterior = []
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            exterior.append([x, y, min_z - 1])
            exterior.append([x, y, max_z + 1])

    for y in range(min_y - 1, max_y + 2):
        for z in range(min_z, max_z + 1):
            exterior.append([min_x - 1, y, z])
            exterior.append([max_x + 1, y, z])

    for z in range(min_z, max_z + 1):
        for x in range(min_x, max_x + 1):
            exterior.append([x, min_y - 1, z])
            exterior.append([x, max_y + 1, z])

    positions_to_test = []
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                if [x, y, z] not in cubes:
                    positions_to_test.append([x, y, z])

    airs = []
    while positions_to_test:
        position = positions_to_test.pop(0)
        [x1, y1, z1] = position
        is_exterior = False
        for [x2, y2, z2] in exterior:
            if ([x1, y1] == [x2, y2] and abs(z1 - z2) == 1) \
                or ([x1, z1] == [x2, z2] and abs(y1 - y2) == 1) \
                or ([y1, z1] == [y2, z2] and abs(x1 - x2) == 1):
                is_exterior = True
                break

        if is_exterior:
            exterior.append(position)
            if position in airs:
                airs.remove(position)
        else:
            airs.append(position)
            positions_to_test.append(position)

        if len(airs) == len(positions_to_test):
            break

    print(len(airs))

    def sort_airs(x, y):
        if x[0] == y[0]:
            if x[1] == y[1]:
                if x[2] == y[2]:
                    return 0
                return -1 if x[2] < y[2] else 1
            return -1 if x[1] < y[1] else 1
        return -1 if x[0] < y[0] else 1

    sorted(airs, key=functools.cmp_to_key(sort_airs))

    for air in airs:
        print(air)


    print(f'Part Two: {part_one_result - getTotalSurfaces(airs)}')
