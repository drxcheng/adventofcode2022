from copy import deepcopy

SAMPLE = False

def dec11(
    _items_by_monkey,
    operation_by_monkey,
    test_divisible_by_monkey,
    test_true_result_by_monkey,
    test_false_result_by_monkey,
    rounds,
    worry_level_change,
):
    items_by_monkey = deepcopy(_items_by_monkey)
    inspected_count_by_monkey = {}

    for _ in range(0, rounds):
        for index in range(0, len(items_by_monkey.keys())):
            while len(items_by_monkey[index]) > 0:
                if index not in inspected_count_by_monkey:
                    inspected_count_by_monkey[index] = 0
                inspected_count_by_monkey[index] += 1
                item = items_by_monkey[index].pop()
                operation = operation_by_monkey[index]
                if operation.startswith('+ '):
                    worry_level = item + (item if operation[2:] == 'old' else int(operation[2:]))
                elif operation.startswith('* '):
                    worry_level = item * (item if operation[2:] == 'old' else int(operation[2:]))
                else:
                    raise
                worry_level = worry_level_change(worry_level)
                if worry_level % test_divisible_by_monkey[index] == 0:
                    items_by_monkey[test_true_result_by_monkey[index]].append(worry_level)
                else:
                    items_by_monkey[test_false_result_by_monkey[index]].append(worry_level)

    inspected_count_by_monkey_sorted = sorted(list(inspected_count_by_monkey.values()), reverse=True)

    return inspected_count_by_monkey_sorted[0] * inspected_count_by_monkey_sorted[1]


items_by_monkey = {}
operation_by_monkey = {}
ultimate_mod = 1
test_divisible_by_monkey = {}
test_true_result_by_monkey = {}
test_false_result_by_monkey = {}


with open(f"dec11{'-sample' if SAMPLE else ''}.txt") as file:
    monkey_index = None

    for line in file:
        line = line.rstrip()
        if line.startswith('Monkey '):
            monkey_index = int(line[7:8])
        elif line.startswith('  Starting items: '):
            items = list(map(lambda x: int(x), line[len('  Starting items: '):].split(', ')))
            items_by_monkey[monkey_index] = items
        elif line.startswith('  Operation: new = old '):
            command = line[len('  Operation: new = old '):]
            operation_by_monkey[monkey_index] = command
        elif line.startswith('  Test: divisible by '):
            test_divisible_by_monkey[monkey_index] = int(line[len('  Test: divisible by '):])
            ultimate_mod *= test_divisible_by_monkey[monkey_index]
        elif line.startswith('    If true: throw to monkey '):
            test_true_result_by_monkey[monkey_index] = int(line[len('    If true: throw to monkey '):])
        elif line.startswith('    If false: throw to monkey '):
            test_false_result_by_monkey[monkey_index] = int(line[len('    If false: throw to monkey '):])
        else:
            continue

    result_part_one = dec11(
        items_by_monkey,
        operation_by_monkey,
        test_divisible_by_monkey,
        test_true_result_by_monkey,
        test_false_result_by_monkey,
        20,
        lambda x: int(x/3),
    )
    print(f'Part One: {result_part_one}')

    result_part_two = dec11(
        items_by_monkey,
        operation_by_monkey,
        test_divisible_by_monkey,
        test_true_result_by_monkey,
        test_false_result_by_monkey,
        10000,
        lambda x: x % ultimate_mod,
    )
    print(f'Part Two: {result_part_two}')
