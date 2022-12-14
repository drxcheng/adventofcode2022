from copy import copy

SAMPLE = False

def move_head(knot_positions, new_x, new_y):
    if knot_positions[0][0] == new_x and knot_positions[0][1] == new_y:
        return knot_positions

    sub_knot_positions = knot_positions[1:]
    if len(sub_knot_positions) > 0:
        next_knot_new_x = knot_positions[1][0]
        next_knot_new_y = knot_positions[1][1]

        x_moved = False
        y_moved = False
        if new_x > next_knot_new_x + 1:
            next_knot_new_x = new_x - 1
            x_moved = True
        elif new_x < next_knot_new_x - 1:
            next_knot_new_x = new_x + 1
            x_moved = True

        if new_y > next_knot_new_y + 1:
            next_knot_new_y = new_y - 1
            y_moved = True
        elif new_y < next_knot_new_y - 1:
            next_knot_new_y = new_y + 1
            y_moved = True

        if x_moved:
            if new_y > knot_positions[1][1]:
                next_knot_new_y = knot_positions[1][1] + 1
            elif new_y < knot_positions[1][1]:
                next_knot_new_y = knot_positions[1][1] - 1

        if y_moved:
            if new_x > knot_positions[1][0]:
                next_knot_new_x = knot_positions[1][0] + 1
            elif new_x < knot_positions[1][0]:
                next_knot_new_x = knot_positions[1][0] - 1

        sub_knot_positions = move_head(sub_knot_positions, next_knot_new_x, next_knot_new_y)

    knot_positions[0][0] = new_x
    knot_positions[0][1] = new_y

    return [knot_positions[0]] + sub_knot_positions

def dec09(lines, number_of_knots):
    knot_positions = [[0, 0] for _ in range(number_of_knots)]
    all_tail_positions = [[0, 0]]

    for line in lines:
        commands = line.split(' ')
        iteration = int(commands[1])
        if commands[0] == 'U':
            for _ in range(iteration):
                knot_positions = move_head(knot_positions, knot_positions[0][0], knot_positions[0][1] + 1)
                all_tail_positions.append(copy(knot_positions[number_of_knots - 1]))
        elif commands[0] == 'R':
            for _ in range(iteration):
                knot_positions = move_head(knot_positions, knot_positions[0][0] + 1, knot_positions[0][1])
                all_tail_positions.append(copy(knot_positions[number_of_knots - 1]))
        elif commands[0] == 'D':
            for _ in range(iteration):
                knot_positions = move_head(knot_positions, knot_positions[0][0], knot_positions[0][1] - 1)
                all_tail_positions.append(copy(knot_positions[number_of_knots - 1]))
        elif commands[0] == 'L':
            for _ in range(iteration):
                knot_positions = move_head(knot_positions, knot_positions[0][0] - 1, knot_positions[0][1])
                all_tail_positions.append(copy(knot_positions[number_of_knots - 1]))
        else:
            raise

    unique_tail_positions = []
    for position in all_tail_positions:
        if position not in unique_tail_positions:
            unique_tail_positions.append(position)

    return len(unique_tail_positions)

with open(f"dec09{f'-sample-{SAMPLE}' if SAMPLE else ''}.txt") as file:
    lines = [line.rstrip() for line in file]
    print(f'Part One: {dec09(lines, 2)}')
    print(f'Part Two: {dec09(lines, 10)}')
