import json
from copy import deepcopy

SAMPLE = False

INPUT_SAMPLE_COMPARE_ASSERTION = [
    ([1,1,3,1,1], [1,1,5,1,1], -1),
    ([[1],[2,3,4]], [[1],4], -1),
    ([9], [[8,7,6]], 1),
    ([[4,4],4,4], [[4,4],4,4,4], -1),
    ([7,7,7,7], [7,7,7], 1),
    ([], [3], -1),
    ([[[]]], [[]], 1),
    ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9], 1),
]

def compare_inputs(input1, input2):
    while True:
        if len(input1) == 0 and len(input2) == 0:
            return 0

        if len(input1) == 0:
            return -1

        if len(input2) == 0:
            return 1

        input1_item = input1.pop(0)
        input2_item = input2.pop(0)

        if isinstance(input1_item, int) and isinstance(input2_item, int):
            if input1_item > input2_item:
                return 1
            if input1_item < input2_item:
                return -1
            continue

        input1_item_list = [input1_item] if isinstance(input1_item, int) else input1_item
        input2_item_list = [input2_item] if isinstance(input2_item, int) else input2_item

        if (result := compare_inputs(input1_item_list, input2_item_list)) != 0:
            return result


for input1, input2, expected in INPUT_SAMPLE_COMPARE_ASSERTION:
    result = compare_inputs(input1, input2)
    assert result == expected, f'{result}'


with open(f"dec13{'-sample' if SAMPLE else ''}.txt") as file:
    lines = [line.rstrip() for line in file]

    iterator = iter(lines)
    sum_of_right_order_indices = 0
    index = 1
    convert_input_to_list = lambda x: json.loads(x)
    all_inputs = [[[2]], [[6]]]

    try:
        while True:
            input1 = convert_input_to_list(next(iterator))
            input2 = convert_input_to_list(next(iterator))

            if compare_inputs(deepcopy(input1), deepcopy(input2)) == -1:
                sum_of_right_order_indices += index

            index += 1

            inserted = False
            for i, v in enumerate(all_inputs):
                if compare_inputs(deepcopy(input1), deepcopy(v)) == -1:
                    all_inputs = all_inputs[0:i] + [input1] + all_inputs[i:]
                    inserted = True
                    break
            if not inserted:
                all_inputs.append(input1)

            inserted = False
            for i, v in enumerate(all_inputs):
                if compare_inputs(deepcopy(input2), deepcopy(v)) == -1:
                    all_inputs = all_inputs[0:i] + [input2] + all_inputs[i:]
                    inserted = True
                    break
            if not inserted:
                all_inputs.append(input2)

            if next(iterator) != '':
                raise
    except StopIteration:
        pass

    print(f'Part One: {sum_of_right_order_indices}')
    print(f'Part Two: {(all_inputs.index([[2]]) + 1) * (all_inputs.index([[6]]) + 1)}')
