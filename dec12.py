SAMPLE = False

def can_up(height_map, current_position, target_position):
    current_letter = height_map[current_position[0]][current_position[1]]
    target_letter = height_map[target_position[0]][target_position[1]]
    if current_letter == 'S':
        current_letter = 'a'
    if target_letter == 'E':
        target_letter = 'z'
    if ord(target_letter) > ord(current_letter) + 1:
        return False
    return True

def can_down(height_map, current_position, target_position):
    current_letter = height_map[current_position[0]][current_position[1]]
    target_letter = height_map[target_position[0]][target_position[1]]
    if current_letter == 'E':
        current_letter = 'z'
    if target_letter == 'S':
        target_letter = 'a'
    if ord(target_letter) < ord(current_letter) - 1:
        return False
    return True

def get_index_from_position(row, column, width):
    return row * width + column

def dijkstra(height_map, start_index, end_index_candidates, can_move):
    step_list = []
    positions_to_process = []
    width = len(height_map[0])
    for i in range(len(height_map) * width):
        step_list.append(None)
        positions_to_process.append(i)
    step_list[start_index] = 0

    def update_step_list(current_index, target_index):
        target_step = step_list[target_index]
        if target_step is None or target_step > step_list[current_index] + 1:
            step_list[target_index] = step_list[current_index] + 1

    while len(positions_to_process) > 0:
        current_index = None
        min_steps = None
        for index in positions_to_process:
            if step_list[index] is not None and (min_steps is None or step_list[index] < min_steps):
                min_steps = step_list[index]
                current_index = index

        if current_index in end_index_candidates:
            return step_list[current_index]

        positions_to_process.remove(current_index)

        row = int(current_index / width)
        column = current_index % width
        if row > 0 and can_move(height_map, [row, column], [row - 1, column]):
            # up
            target_index = get_index_from_position(row - 1, column, width)
            if target_index in positions_to_process:
                update_step_list(current_index, target_index)

        if column < width - 1 and can_move(height_map, [row, column], [row, column + 1]):
            # right
            target_index = get_index_from_position(row, column + 1, width)
            if target_index in positions_to_process:
                update_step_list(current_index, target_index)

        if row < len(height_map) - 1 and can_move(height_map, [row, column], [row + 1, column]):
            # down
            target_index = get_index_from_position(row + 1, column, width)
            if target_index in positions_to_process:
                update_step_list(current_index, target_index)

        if column > 0 and can_move(height_map, [row, column], [row, column - 1]):
            # left
            target_index = get_index_from_position(row, column - 1, width)
            if target_index in positions_to_process:
                update_step_list(current_index, target_index)

with open(f"dec12{'-sample' if SAMPLE else ''}.txt") as file:
    height_map = []
    start_index = None
    end_index = None
    trail_start_index_candidates = []
    width = 0
    row = 0

    for line in file:
        line = line.rstrip()
        width = len(line)
        height_map.append([*line])

        if 'a' in line:
            trail_start_index_candidates.append(get_index_from_position(row, line.index('a'), width))

        if 'S' in line:
            start_index = get_index_from_position(row, line.index('S'), width)
            trail_start_index_candidates.append(start_index)

        if 'E' in line:
            end_index = get_index_from_position(row, line.index('E'), width)

        row += 1

    shortest_steps = dijkstra(height_map, start_index, [end_index], can_up)
    print(f'Part One: {shortest_steps}')

    shortest_steps = dijkstra(height_map, end_index, trail_start_index_candidates, can_down)
    print(f'Part Two: {shortest_steps}')
