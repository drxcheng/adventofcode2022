SAMPLE = False

DIRECTIONS = ['N', 'S', 'W', 'E']

with open(f"dec23{'-sample' if SAMPLE else ''}.txt") as file:
    elf_positions = []

    y = 0
    for line in file:
        line = line.rstrip()
        for x, char in enumerate(line):
            if char == '#':
                elf_positions.append([x, y])
        y += 1

    def should_stay(position, fields):
        x, y = position
        return ((y - 1) not in fields or (
            not fields[y - 1].get(x - 1, False) \
            and not fields[y - 1].get(x, False) \
            and not fields[y - 1].get(x + 1, False)
        )) and ((y + 1) not in fields or (
            not fields[y + 1].get(x - 1, False) \
            and not fields[y + 1].get(x, False) \
            and not fields[y + 1].get(x + 1, False)
        )) and not fields[y].get(x - 1, False) \
            and not fields[y].get(x + 1, False)

    last_direction = 'E'
    round = 0
    while True:
        print(f'round{round+1}')
        fields = {}
        for x, y in elf_positions:
            if y not in fields:
                fields[y] = {}
            fields[y][x] = True
        done = True
        elf_proposals = []
        new_elf_positions = []
        index_to_revert = []
        for index, elf in enumerate(elf_positions):
            x, y = elf_positions[index]
            proposal = None
            position = [x, y]
            if should_stay([x, y], fields):
                new_elf_positions.append(position)
                continue
            done = False
            for incr in range(1, 5):
                next_direction = DIRECTIONS[(DIRECTIONS.index(last_direction) + incr) % 4]
                if next_direction == 'N' \
                    and ((y - 1) not in fields or (
                        not fields[y - 1].get(x - 1, False) \
                        and not fields[y - 1].get(x, False) \
                        and not fields[y - 1].get(x + 1, False))):
                        proposal = next_direction
                        position = [x, y - 1]
                        break
                if next_direction == 'S' \
                    and ((y + 1) not in fields or (
                        not fields[y + 1].get(x - 1, False) \
                        and not fields[y + 1].get(x, False) \
                        and not fields[y + 1].get(x + 1, False))):
                        proposal = next_direction
                        position = [x, y + 1]
                        break
                if next_direction == 'W' \
                    and ((y - 1) not in fields or not fields[y - 1].get(x - 1, False)) \
                    and (not fields[y].get(x - 1, False)) \
                    and ((y + 1) not in fields or not fields[y + 1].get(x - 1, False)):
                        proposal = next_direction
                        position = [x - 1, y ]
                        break
                if next_direction == 'E' \
                    and ((y - 1) not in fields or not fields[y - 1].get(x + 1, False)) \
                    and (not fields[y].get(x + 1, False)) \
                    and ((y + 1) not in fields or not fields[y + 1].get(x + 1, False)):
                        proposal = next_direction
                        position = [x + 1, y]
                        break
            if proposal is None:
                new_elf_positions.append(position)
            else:
                try:
                    ind = new_elf_positions.index(position)
                    # failed
                    index_to_revert.append(ind)
                    new_elf_positions.append([x, y])
                except ValueError:
                    # good for now
                    new_elf_positions.append(position)

        if done:
            round += 1
            break

        for index in index_to_revert:
            new_elf_positions[index] = elf_positions[index]

        # print(f'end: {new_elf_positions}')
        elf_positions = new_elf_positions
        last_direction = DIRECTIONS[(DIRECTIONS.index(last_direction) + 1) % 4]
        round += 1

        if round == 10:
            min_x = None
            min_y = None
            max_x = None
            max_y = None
            for x, y in elf_positions:
                if min_x is None or x < min_x:
                    min_x = x
                if max_x is None or x > max_x:
                    max_x = x
                if min_y is None or y < min_y:
                    min_y = y
                if max_y is None or y > max_y:
                    max_y = y

            number_of_spaces = (max_x - min_x + 1) * (max_y - min_y + 1)
            print(f'Part One: {number_of_spaces - len(elf_positions)}')

    print(f'Part Two: {round}')
