SAMPLE = False

AIR = '.'
ROCK = '#'
SAND = 'o'

rock_sand_map = {}
min_x = 500
max_x = 0
max_y = 0

with open(f"dec14{'-sample' if SAMPLE else ''}.txt") as file:
    for line in file:
        line = line.rstrip()
        last_x = 500
        last_y = 0
        is_first = True
        for point in line.split('->'):
            [x, y] = list(map(int, point.strip().split(',')))
            # print(x, y)
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

            if x == last_x:
                if y > last_y:
                    for i in range(last_y + 1, y + 1):
                        if i not in rock_sand_map:
                            rock_sand_map[i] = {}
                        rock_sand_map[i][x] = ROCK
                elif y < last_y:
                    for i in range(y, last_y):
                        if i not in rock_sand_map:
                            rock_sand_map[i] = {}
                        rock_sand_map[i][x] = ROCK
                else:
                    raise
            elif y == last_y:
                if y not in rock_sand_map:
                    rock_sand_map[y] = {}
                if x > last_x:
                    for i in range(last_x + 1, x + 1):
                        rock_sand_map[y][i] = ROCK
                elif x < last_x:
                    for i in range(x, last_x):
                        rock_sand_map[y][i] = ROCK
                else:
                    raise
            elif is_first:
                last_y = y
                last_x = x
                is_first = False

                if y not in rock_sand_map:
                    rock_sand_map[y] = {}
                rock_sand_map[y][x] = ROCK
            else:
                raise

            last_y = y
            last_x = x

    sand_index = 0
    is_part_one_bottom = False
    sand_index_part_one = None
    blocked = False
    while True:
        sand_x = 500
        sand_y = 0
        while True:
            if sand_y == max_y + 1 \
                or ((sand_y + 1) in rock_sand_map \
                and rock_sand_map[sand_y + 1].get(sand_x) \
                and rock_sand_map[sand_y + 1].get(sand_x - 1) \
                and rock_sand_map[sand_y + 1].get(sand_x + 1)):
                # rest
                if sand_y not in rock_sand_map:
                    rock_sand_map[sand_y] = {}
                rock_sand_map[sand_y][sand_x] = SAND
                if sand_x < min_x:
                    min_x = sand_x
                if sand_x > max_x:
                    max_x = sand_x
                # print(f'sand {sand_index}: rest at ({sand_x}, {sand_y})')
                if sand_x == 500 and sand_y == 0:
                    blocked = True
                break

            if sand_y == max_y and is_part_one_bottom is False:
                is_part_one_bottom = True
                sand_index_part_one = sand_index
                break

            if (sand_y + 1) not in rock_sand_map or rock_sand_map[sand_y + 1].get(sand_x) is None:
                # down
                sand_y += 1
            elif rock_sand_map[sand_y + 1].get(sand_x - 1) is None:
                # down left
                sand_y += 1
                sand_x -= 1
            elif rock_sand_map[sand_y + 1].get(sand_x + 1) is None:
                # down right
                sand_y += 1
                sand_x += 1
            # else continue
        if blocked:
            break
        sand_index += 1

    for y in range(0, max_y + 3):
        for x in range (min_x, max_x + 1):
            if y in rock_sand_map and x in rock_sand_map[y]:
                print(rock_sand_map[y][x], end='')
            elif y == 0 and x == 500:
                print('+', end='')
            elif y == max_y + 2:
                print('=', end='')
            else:
                print('.', end='')
        print('')

    print(f'Part One: {sand_index_part_one}')
    print(f'Part Two: {sand_index}')
