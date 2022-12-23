SAMPLE = False

DIRECTIONS = ['N', 'S', 'W', 'E']

with open(f"dec23{'-sample' if SAMPLE else ''}.txt") as file:
    elf_positions = []
    fields = {}

    y = 0
    for line in file:
        fields[y] = {}
        line = line.rstrip()
        for x, char in enumerate(line):
            if char == '#':
                elf_positions.append([x, y])
                fields[y][x] = True
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
        elf_proposals = []
        done = True
        for index, elf in enumerate(elf_positions):
            x, y = elf_positions[index]
            proposal = None
            if should_stay([x, y], fields):
                elf_proposals.append(None)
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
                        break
                if next_direction == 'S' \
                    and ((y + 1) not in fields or (
                        not fields[y + 1].get(x - 1, False) \
                        and not fields[y + 1].get(x, False) \
                        and not fields[y + 1].get(x + 1, False))):
                        proposal = next_direction
                        break
                if next_direction == 'W' \
                    and ((y - 1) not in fields or not fields[y - 1].get(x - 1, False)) \
                    and (not fields[y].get(x - 1, False)) \
                    and ((y + 1) not in fields or not fields[y + 1].get(x - 1, False)):
                        proposal = next_direction
                        break
                if next_direction == 'E' \
                    and ((y - 1) not in fields or not fields[y - 1].get(x + 1, False)) \
                    and (not fields[y].get(x + 1, False)) \
                    and ((y + 1) not in fields or not fields[y + 1].get(x + 1, False)):
                        proposal = next_direction
                        break
            elf_proposals.append(proposal)

        # print(elf_proposals)

        if done:
            round += 1
            break

        new_elf_positions = []
        for index, elf in enumerate(elf_positions):
            x, y = elf_positions[index]
            proposal = elf_proposals[index]
            if proposal == 'N':
                y -= 1
            elif proposal == 'S':
                y += 1
            elif proposal == 'W':
                x -= 1
            elif proposal == 'E':
                x += 1
            new_elf_positions.append([x, y])

        failed_proposals = []
        for index, new_position in enumerate(new_elf_positions):
            if index == len(new_elf_positions) - 1 or index in failed_proposals:
                continue
            for sub_index, position in enumerate(new_elf_positions[index + 1:]):
                if new_position == position:
                    failed_proposals.append(index)
                    failed_proposals.append(index + 1 + sub_index)

        for index in failed_proposals:
            x, y = new_elf_positions[index]
            proposal = elf_proposals[index]
            if proposal == 'N':
                y += 1
            elif proposal == 'S':
                y -= 1
            elif proposal == 'W':
                x += 1
            elif proposal == 'E':
                x -= 1
            new_elf_positions[index] = [x, y]

        elf_positions = new_elf_positions
        fields = {}
        for x, y in elf_positions:
            if y not in fields:
                fields[y] = {}
            fields[y][x] = True

        # print(elf_positions)
        # print(fields)
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
