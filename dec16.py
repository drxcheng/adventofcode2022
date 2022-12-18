from copy import deepcopy

SAMPLE = False

with open(f"dec16{'-sample' if SAMPLE else ''}.txt") as file:
    all_valves = []
    distance_map = {}
    rate_by_valve = {}
    closed_valves = []

    for line in file:
        parts = line.rstrip().split(' ')
        valve = parts[1]
        rate = int(parts[4][5:-1])

        rate_by_valve[valve] = rate
        if rate > 0:
            closed_valves.append(valve)
        if valve not in distance_map:
            distance_map[valve] = {valve: 0}
        for connect_to in parts[9:]:
            distance_map[valve][connect_to[:2]] = 1

    all_valves = list(rate_by_valve.keys())

    for start_valve in all_valves:
        valves_to_process = [valve for valve in all_valves if valve != start_valve]
        while len(valves_to_process) > 0:
            shortest_distance = None
            closest_valve = None

            for valve in valves_to_process:
                distance = distance_map[start_valve].get(valve)
                if distance is None:
                    continue

                if shortest_distance is None or distance < shortest_distance:
                    closest_valve = valve
                    shortest_distance = distance

            if closest_valve is None:
                raise
            valves_to_process.remove(closest_valve)

            for valve in distance_map[closest_valve].keys():
                if valve in valves_to_process:
                    new_distance = distance_map[start_valve][closest_valve] + distance_map[closest_valve][valve]
                    if valve not in distance_map[start_valve] or new_distance < distance_map[start_valve][valve]:
                        distance_map[start_valve][valve] = new_distance
        for valve, distance in distance_map[start_valve].items():
            if valve != start_valve:
                distance_map[valve][start_valve] = distance_map[start_valve][valve]

    # for valve, distance in distance_map.items():
    #     print(f'from {valve}: {distance}')
    # print(rate_by_valve)
    # print(closed_valves)

    all_pressure_released = {}

    def next_step(
        current_valve,
        sub_closed_valves,
        pressure_release_rate,
        pressure_released,
        steps_remaining,
        sequence,
    ):
        possible_next_valves = [valve for valve in sub_closed_valves if distance_map[current_valve][valve] + 1 < steps_remaining]

        if not possible_next_valves:
            key = ','.join(sequence)
            all_pressure_released[key] = pressure_released + pressure_release_rate * steps_remaining
            return

        for next_valve in possible_next_valves:
            distance = distance_map[current_valve][next_valve]
            new_sub_closed_valves = deepcopy(sub_closed_valves)
            new_sub_closed_valves.remove(next_valve)
            new_sequence = deepcopy(sequence)
            new_sequence.append(next_valve)
            next_step(
                next_valve,
                new_sub_closed_valves,
                pressure_release_rate + rate_by_valve[next_valve],
                pressure_released + pressure_release_rate * (distance + 1),
                steps_remaining - distance - 1,
                new_sequence,
            )

    if all_valves[0] in closed_valves:
        closed_valves.remove(all_valves[0])
        next_step(
            all_valves[0],
            closed_valves,
            rate_by_valve[all_valves[0]],
            rate_by_valve[all_valves[0]],
            29,
            [all_valves[0] + 'o'],
        )
    else:
        next_step(
            all_valves[0],
            closed_valves,
            0,
            0,
            30,
            [all_valves[0]],
        )

    max_pressure = 0
    for sequence, val in all_pressure_released.items():
        if val > max_pressure:
            max_pressure = val
        # print(f'{sequence}: {val}')

    print(f'Part One: {max_pressure}')
    # print(f'Part Two: ')
