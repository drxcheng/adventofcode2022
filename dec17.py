from copy import deepcopy

SAMPLE = False

WIDTH = 7
TOTAL_ROCKS_PART_ONE = 2022
TOTAL_ROCKS_PART_TWO = 1000000000000

with open(f"dec17{'-sample' if SAMPLE else ''}.txt") as file:
    jet_pattern = ''
    for line in file:
        if jet_pattern:
            raise
        jet_pattern = line.rstrip()

    rock_start_positions = [
        [[2,3], [3,3], [4,3], [5,3]],
        [[3,3], [2,4], [3,4], [4,4], [3,5]],
        [[2,3], [3,3], [4,3], [4,4], [4,5]],
        [[2,3], [2,4], [2,5], [2,6]],
        [[2,3], [3,3], [2,4], [3,4]],
    ]

    stopped_rock_postions = []

    def can_shift_right(rock_position):
        if right + 1 >= WIDTH:
            return False
        for point in rock_position:
            if [point[0] + 1, point[1]] in stopped_rock_postions:
                return False
        return True

    def can_shift_left(rock_position):
        if left - 1 < 0:
            return False
        for point in rock_position:
            if [point[0] - 1, point[1]] in stopped_rock_postions:
                return False
        return True

    def can_drop(rock_position):
        if rock_position[0][1] <= 0:
            return False
        for point in rock_position:
            if [point[0], point[1] - 1] in stopped_rock_postions:
                return False
        return True

    def print_map(rock_position):
        for y in reversed(range(rock_position[-1][1] + 1)):
            for x in range(7):
                if [x, y] in rock_position:
                    print('@', end='')
                elif [x, y] in stopped_rock_postions:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')

    step = 0
    height = -1
    rock_position = None
    for rock_index in range(0, TOTAL_ROCKS_PART_ONE + 1):
        height = max(height, rock_position[-1][1] + 1 if rock_position is not None else 0)

        rock_position = deepcopy(rock_start_positions[rock_index % 5])
        left = WIDTH
        right = 0
        for point in rock_position:
            point[1] += height
            if point[0] < left:
                left = point[0]
            if point[0] > right:
                right = point[0]

        while True:
            if jet_pattern[step] == '>':
                if can_shift_right(rock_position):
                    left += 1
                    right += 1
                    for point in rock_position:
                        point[0] += 1
            elif jet_pattern[step] == '<':
                if can_shift_left(rock_position):
                    left -= 1
                    right -= 1
                    for point in rock_position:
                        point[0] -= 1
            else:
                raise

            step = (step + 1) % len(jet_pattern)

            if can_drop(rock_position):
                for point in rock_position:
                    point[1] -= 1
            else:
                stopped_rock_postions += rock_position
                break

    print(f'Part One: {height}')
    # print(f'Part Two: {height}')
