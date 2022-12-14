SAMPLE = False

with open(f"dec10{'-sample' if SAMPLE else ''}.txt") as file:
    x = 1
    cycle_value = [x]

    for line in file:
        line = line.rstrip()

        commands = line.split(' ')
        if commands[0] == 'noop':
            cycle_value.append(x)
        elif commands[0] == 'addx':
            cycle_value.append(x)
            x += int(commands[1])
            cycle_value.append(x)
        else:
            raise

    signal_strength = 0
    for cycle in range(20, 221, 40):
        signal_strength += cycle * cycle_value[cycle - 1]

    print(f'Part One: {signal_strength}')

    lit_dark = []
    for i in range(0, len(cycle_value)):
        sprite_positions = [cycle_value[i] - 1, cycle_value[i], cycle_value[i] + 1]
        scan_position = (i) % 40
        if scan_position in sprite_positions:
            lit_dark.append('#')
        else:
            lit_dark.append('.')

    print('Part Two:')
    for i in range(1, len(lit_dark)):
        if (i) % 40 == 0:
            print(lit_dark[i - 1])
        else:
            print(lit_dark[i - 1], end='')
