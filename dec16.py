SAMPLE = True

with open(f"dec16{'-sample' if SAMPLE else ''}.txt") as file:
    for line in file:
        line = line.rstrip()
        print(line)

    print(f'Part One: ')
    print(f'Part Two: ')
