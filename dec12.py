from copy import deepcopy

INPUT = '''abcccaaaaacccacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaacaccccccaaacccccccccccccccccccccccccccccccccccaaaaaaaaccccccccccccccccccccccccccccccccaaaaaa
abcccaaaaacccaaacaaacccccccccccccccccaaccccccacccaacccccccccccaacccccaaaaaaaaaaaccaaaaaaccccccccccccccccccccccccccccccccccaaaaaccccccccccccccccccccccccccccccccccaaaaaa
abccccaaaaaccaaaaaaaccccccccccccccaaaacccccccaacaaacccccccccaaaaaacccaaaaaaaaaaaccaaaaaacccccccccccccccccccccccccccccccccccaaaaaccccccccccccccaaacccccccccccccccccaaaaa
abccccaacccccaaaaaacccccccccccccccaaaaaacccccaaaaaccccccccccaaaaaacaaaaaaaaaaaaaccaaaaaacccccccccccccccccccccccccccccccccccaacaaccccccccccccccaaaaccccccccccccccccccaaa
abccccccccccaaaaaaaacccccccccccaaccaaaaaccccccaaaaaacccccccccaaaaacaaaaaaaaccccccccaaaaacccccccccccccccccccccccccccccccccccaacccccccccccccccccaaaaccaaacccccccccccccaac
abaaaaaccccaaaaaaaaaaccccccaaccaacaaaaacccccaaaaaaaaaaacccccaaaaacaaaacaaaaacccccccaacaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaaaaaaacccccccccccaaac
abaaaaaccccaaaaaaaaaacaacccaaaaaacaccaacccccaaaaaaaaaaacccccaaaaaccccccaaaaaccccccccccaacccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaakkkllccccccccccccccc
abaaaaacccccccaaacaaaaaaccccaaaaaaaccccccaaacccaacccaaaaaaacccccccccccccaaaaacccccccccaaaaaaccccccccccccccccccccccccccaaccccccccccccccccccccccackkkkkklllccccaaaccccccc
abaaaaacccccccaaacaaaaaaacccaaaaaaaccccccaaaacaaacaaaaaaaacccccccccccccaaaaaacccccccccaaaaaaccaacaacccccccccccccccaaaaaacccccccccccccccccccaaakkkkkkkkllllcccaaacaccccc
abaaaaaccccccccaacaaaaaaaacaaaaaaccccccccaaaaaaacaaaaaaaaacccccccccccccaaaacccccccccaaaaaaacccaaaaacccccccccccccccaaaaaaccccccccccccccccjjjjjkkkkkkpppplllcccaaaaaacccc
abaaaccccccccccccccaaaaaaacaaaaaacccccccccaaaaaaccaaaaaaaccccccccccccccccaaaccccccccaaaaaaaccccaaaaacccccccccccccccaaaaaaaccccaaccccccjjjjjjjkkkkppppppplllcccaaaaacccc
abccccccccccccccccaaaaaacccccccaaccccccaaaaaaaacccccaaaaaaccccccccccccccccccccccccccccaaaaaaccaaaaaacccccccccccccccaaaaaaaaaacaacccccjjjjjjjjjkooppppppplllcccaaacccccc
abccccccccccccccccaaaaaacccccccccccccccaaaaaaaaacccaaacaaacccccccccccccccccccccccaaaccaaccaaccaaaaccccccccccccccccaaaaaaaccaaaaaccccjjjjooooooooopuuuupppllccccaaaccccc
abccccccccccccccccccccaaccccccccccccccccaaaaaaaacccaaaccaacccccccccccccccccccccccaaaaaaacccccccaaaccccccccccccccccaaaaaaccccaaaaaaccjjjoooooooooouuuuuupplllccccaaccccc
abccaaaaccccaaacccccccccccccccccccccccccccaaaaaaaccaaccccccccccccaacccccccccccccccaaaaacccaaccaaaccccccccccccccccccccaaacccaaaaaaaccjjjoootuuuuuuuuuuuuppllllccccaccccc
abccaaaaaccaaaacccccccccccccccccccccccccccaacccacccccccccccccccacaaaacccccccccccaaaaaaacccaaaaaaacccccccccccccccccccccccccaaaaaacccciijnoottuuuuuuxxyuvpqqlmmcccccccccc
abcaaaaaaccaaaacccccccaaaaccccccccccacccccaaccccaaaccccccccccccaaaaaacccccccccccaaaaaaaaccaaaaaacccccccccccccccccaacccccccaacaaacccciiinntttxxxxuxxyyvvqqqqmmmmddddcccc
abcaaaaaacccaaacccccccaaaaccccaaaaaaaaccaaaaccccaacaacccccccccccaaaaccccccccccccaaaaaaaacccaaaaaaaacccccccccccccaaaaccccccccccaacccciiinntttxxxxxxxyyvvqqqqqmmmmdddcccc
abcaaaaaacccccccccccccaaaacccccaaaaaacccaaaaaaaaaaaaacccccccccccaaaaccccccccccccccaaacacccaaaaaaaaacccccccccccccaaaacccccccccccccccciiinnnttxxxxxxxyyvvvvqqqqmmmdddcccc
abcccaaccccccccccccccccaaccccccaaaaaacccaaaaaaaaaaaaaaccccccccccaacaccccccccccccccaaaccccaaaaaaaaaacccccccccccccaaaacccccccccccccccciiinnntttxxxxxyyyyyvvvqqqqmmmdddccc
SbccccccccccccccccccccccccccccaaaaaaaaccaaaccaaaaaaaaacccccccccccccccccccccccccccccccccccaaaaaaacccccccccaacccccccccccccccccccccccccciiinntttxxxxEzyyyyyvvvqqqmmmdddccc
abcccccccccccccccccccccccccccaaaaaaaaaacccccccaaaaaacccccccccccccaaacccccaacaacccccccccccccccaaaaaaccccccaacaaacccccccccccccccccccccciiinntttxxxyyyyyyyvvvvqqqmmmdddccc
abcccccccccccccccccccccccccccaaaaaaaaaaccccccaaaaaaaaccccccccccccaaaccccccaaaacccccccccccccccaaaaaaccccccaaaaacccccccccccccccccccccciiinnnttxxyyyyyyyvvvvvqqqqmmmdddccc
abcccccccccccccccccccccccccccacacaaacccccccccaaaaaaacccccccccccaaaaaaaacccaaaaacccccccccccccccaaaaaaaacaaaaaaccccccccccccccccccccccciiinntttxxwyyyyywwvvrrrqqmmmdddcccc
abaccccccccccccccccccccccccccccccaaacccccccccaaacaaaaacccccccccaaaaaaaaccaaaaaacccccccccccccccaaaaaaaacaaaaaaacccccccccccccccccccccchhnnnttwwwwwwwyyywvrrrrnnnnmdddcccc
abaccccccccccccccccccccccccccccccaaccccccccccccccaaaaaacccccccccaaaaaccccaaaacaccccccccccccccccaaaaacccccaaaaaaccccccaaaccccccaaaccchhnmmttswwwwwwywwwrrrrnnnnneeeccccc
abaccccccccccccccccccccccccccccccccccccccccccccccaaaaaacccccaaccaaaaaacccccaaccccccccccccccccccaaaaaaccccaaccaaccccaaaaaacccccaaacahhhmmmsssssssswwwwwrrrnnnneeeecccccc
abaaaccccccccccccccccccccccccccccaaaccccccccccccccaaaaaccccaaaccaaaaaacccccccccccccccccccccccccaaaaaaccccaaccccccccaaaaaacccaaaaaaahhhmmmmsssssssswwwwrrnnnneeeeacccccc
abaaaccccccccccccccccccccccccccccaaaaaaccccccccccaaaaacaaaaaaaccaaaccaccccccccaaaaaccccccccccccaaaacacccccccccccccccaaaaacccaaaaaaahhhhmmmmssssssswwwwrrnnneeeeaacccccc
abaaacccccccccccccccccccccccccccaaaaaaaccccccccccaaaaacaaaaaaaaaacccaaaaacccccaaaaacccccccccacaaaaaccacccccccccccccaaaaacccccaaaaaachhhmmmmmmmmmsssrrrrrnnneeeaaaaacccc
abaccccccccccccccaaaaccccccccccaaaaaaaacccccccccccccccccaaaaaaaaacccaaaaaccccaaaaaacccccccccaaaaaaaaaacccccccccccccaaaaaccccccaaaaachhhhmmmmmmmooossrrronneeeaaaaaacccc
abaccccccccccccccaaaaccccccccccaaaaaaacccccccccccccccccccaaaaaaaccccaaaaaacccaaaaaaccccaaaccaaaaaaaaaacccccccccccaaccccccccccaaaaaacchhhhhggggooooorrroonnfeeaaaaaccccc
abcccccccccccccccaaaaccccccccccccaaaaaacccccccccccccccccaaaaaaccccccaaaaaacccaaaaaaccccaaaaaacaaaaaacccccccccaaccaacccccccccccaacccccchhhhggggggoooooooooffeaaaaacccccc
abccccccccccccccccaacccccccccccccaaaaaacccccccaaccacccccaaaaaaacccccaaaaaaccccaaaccccccaaaaaacaaaaaacccccccccaaaaacccccccccccccccccccccccgggggggggooooooffffaaaaaaccccc
abccccccccccccccccccccccccccaaaccaacccccccccccaaaaacccccaaccaaacccccccaaacccccccccccccaaaaaaacaaaaaacccccccccaaaaaaaaccccccccccccccccccccccaaaggggfooooffffccccaacccccc
abaaccccccccccccccccccccccccaaacaccccccccccccaaaaacccccccccccaacccccccaaaacccaacccccccaaaaaaaaaaaaaaaccccccccccaaaaacccccccccccccaaaccccccccccccggfffffffffcccccccccccc
abaaccccccccccccccccccccccaacaaaaacccccccccccaaaaaacccccccccccccccccccaaaacaaaacccccccaaaaaaaaaccccaccccccccccaaaaaccccccccccccccaaaccccccccccccagfffffffccccccccccccca
abaacccccccaacccccccccccccaaaaaaaaccccccaacccccaaaacccccccccccccccccccaaaaaaaaacccccccccaaacaacaaacccccccccccaaacaaccccaaccaaccaaaaaaaaccccccccaaaccffffcccccccccccccaa
abaaaaaaaccaaccccccccccccccaaaaacccccccaaaacccaaccccccccccccccccccacaaaaaaaaaaccccccccccaaacaaaaaacccccccccccccccaaccccaaaaaaccaaaaaaaacccccccccaacccccccccccccccaaacaa
abaaaaaaaaaaccccccccccccccccaaaaaccccccaaaacccccccccccccccccccccccaaaaaaaaaaaaccccccccccccccaaaaaacccccccccccccccccccccaaaaaacccaaaaaacccccccccaaacccccccccccccccaaaaaa
abaaaacaaaaaaaacccccccccccccaacaaccccccaaaaccccccccccccccccccccccccaaaaaaaaaaacccccccccccccaaaaaaaacccccccccccccccccccaaaaaaaaccaaaaaaccccccccccccccccccccccccccccaaaaa'''

INPUT_SAMPLE = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

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


def process(height_map, step_list, destinations, can_move):
    width = len(height_map[0])

    def update_step_list(current_index, target_index):
        target_step = step_list[target_index]
        if target_step is None or target_step > step_list[current_index] + 1:
            step_list[target_index] = step_list[current_index] + 1

    while True:
        for index in range(0, len(step_list)):
            if step_list[index] is None:
                continue

            row = int(index / width)
            column = index % width

            reached_destinations = []
            if row > 0 and can_move(height_map, [row, column], [row - 1, column]):
                # up
                target_index = get_index_from_position(row - 1, column, width)
                update_step_list(index, target_index)
                if target_index in destinations:
                    reached_destinations.append(target_index)

            if column < width - 1 and can_move(height_map, [row, column], [row, column + 1]):
                # right
                target_index = get_index_from_position(row, column + 1, width)
                update_step_list(index, target_index)
                if target_index in destinations:
                    reached_destinations.append(target_index)

            if row < len(height_map) - 1 and can_move(height_map, [row, column], [row + 1, column]):
                # down
                target_index = get_index_from_position(row + 1, column, width)
                update_step_list(index, target_index)
                if target_index in destinations:
                    reached_destinations.append(target_index)

            if column > 0 and can_move(height_map, [row, column], [row, column - 1]):
                # left
                target_index = get_index_from_position(row, column - 1, width)
                update_step_list(index, target_index)
                if target_index in destinations:
                    reached_destinations.append(target_index)

            if reached_destinations:
                return min([step_list[destination] for destination in reached_destinations])


def main():
    height_map = []
    initial_step_list = []
    start_index = None
    end_index = None
    trail_start_index_candidates = []

    width = 0
    row = 0
    for line in INPUT.split('\n'):
        width = len(line)
        height_map.append([*line])
        for _ in range(len(line)):
            initial_step_list.append(None)

        if 'a' in line:
            trail_start_index_candidates.append(get_index_from_position(row, line.index('a'), width))

        if 'S' in line:
            start_index = get_index_from_position(row, line.index('S'), width)
            trail_start_index_candidates.append(start_index)

        if 'E' in line:
            end_index = get_index_from_position(row, line.index('E'), width)

        row += 1

    step_list = deepcopy(initial_step_list)
    step_list[start_index] = 0

    result_part_one = process(
        height_map,
        step_list,
        [end_index],
        can_up,
    )
    print(f'Part One: {result_part_one}')

    highest_start = 0
    for row, line in enumerate(height_map):
        for column, char in enumerate([*line]):
            if char == 'a':
                step = step_list[get_index_from_position(row, column, width)]
                print(step)
                if step > highest_start:
                    highest_start = step
    # print(highest_start)

    print(f'Part Two: {result_part_one - highest_start + 1}')

    # step_list = deepcopy(initial_step_list)
    # step_list[end_index] = 0

    # print(f'''Part Two: {process(
    #     height_map,
    #     step_list,
    #     trail_start_index_candidates,
    #     can_down,
    # )}''')

main()
