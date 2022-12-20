SAMPLE = False

def mix(numbers, positions):
    for ind, val in enumerate(numbers):
        if val == 0:
            continue

        index_of_ind = positions.index(ind)
        positions.pop(index_of_ind)

        insert_at = (index_of_ind + val) % (len(numbers) - 1)
        if insert_at == 0:
            insert_at = len(numbers) - 1
        positions.insert(insert_at, ind)

    return positions

def part_one(initial_numbers):
    positions = [i for i in range(len(initial_numbers))]
    positions = mix(initial_numbers, positions)
    final_numbers = [initial_numbers[ind] for ind in positions]

    return final_numbers

def part_two(initial_numbers):
    initial_numbers = list(map(lambda x: x * 811589153, initial_numbers))
    positions = [i for i in range(len(initial_numbers))]
    for _ in range(10):
        positions = mix(initial_numbers, positions)
        new_numbers = [initial_numbers[ind] for ind in positions]

    return new_numbers

def get_coordinate_sum(numbers):
    index_of_zero = numbers.index(0)
    first_coordinates_index = (index_of_zero + 1000) % len(numbers)
    first_coordinates = numbers[first_coordinates_index]
    second_coordinates_index = (index_of_zero + 2000) % len(numbers)
    second_coordinates = numbers[second_coordinates_index]
    third_coordinates_index = (index_of_zero + 3000) % len(numbers)
    third_coordinates = numbers[third_coordinates_index]

    return first_coordinates + second_coordinates + third_coordinates

with open(f"dec20{'-sample' if SAMPLE else ''}.txt") as file:
    initial_numbers = [int(line.rstrip()) for line in file]

    print(f'Part One: {get_coordinate_sum(part_one(initial_numbers))}')
    print(f'Part Two: {get_coordinate_sum(part_two(initial_numbers))}')
