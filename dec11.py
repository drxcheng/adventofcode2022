INPUT = '''Monkey 0:
  Starting items: 99, 63, 76, 93, 54, 73
  Operation: new = old * 11
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 1:
  Starting items: 91, 60, 97, 54
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 3
    If false: throw to monkey 2

Monkey 2:
  Starting items: 65
  Operation: new = old + 7
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 5

Monkey 3:
  Starting items: 84, 55
  Operation: new = old + 3
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 4:
  Starting items: 86, 63, 79, 54, 83
  Operation: new = old * old
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 0

Monkey 5:
  Starting items: 96, 67, 56, 95, 64, 69, 96
  Operation: new = old + 4
  Test: divisible by 5
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 6:
  Starting items: 66, 94, 70, 93, 72, 67, 88, 51
  Operation: new = old * 5
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 5

Monkey 7:
  Starting items: 59, 59, 74
  Operation: new = old + 8
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 3'''

INPUT_SAMPLE = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

def main():
    items_by_monkey = {}
    operation_by_monkey = {}
    test_divisible_by_monkey = {}
    test_true_result_by_monkey = {}
    test_false_result_by_monkey = {}
    inspected_count_by_monkey = {}

    monkey_index = None
    for line in INPUT_SAMPLE.split('\n'):
        # print(line)
        if line.startswith('Monkey '):
            monkey_index = int(line[7:8])
            inspected_count_by_monkey[monkey_index] = 0
        elif line.startswith('  Starting items: '):
            items = list(map(lambda x: int(x), line[len('  Starting items: '):].split(', ')))
            items_by_monkey[monkey_index] = items
        elif line.startswith('  Operation: new = old '):
            command = line[len('  Operation: new = old '):]
            operation_by_monkey[monkey_index] = command
        elif line.startswith('  Test: divisible by '):
            test_divisible_by_monkey[monkey_index] = int(line[len('  Test: divisible by '):])
        elif line.startswith('    If true: throw to monkey '):
            test_true_result_by_monkey[monkey_index] = int(line[len('    If true: throw to monkey '):])
        elif line.startswith('    If false: throw to monkey '):
            test_false_result_by_monkey[monkey_index] = int(line[len('    If false: throw to monkey '):])
        else:
            continue

    for round in range(0, 20):
        for index in range(0, monkey_index + 1):
            # print(f'Monkey {index}')
            while len(items_by_monkey[index]) > 0:
                inspected_count_by_monkey[index] += 1
                item = items_by_monkey[index].pop()
                operation = operation_by_monkey[index]
                if operation.startswith('+ '):
                    worry_level = item + (item if operation[2:] == 'old' else int(operation[2:]))
                elif operation.startswith('* '):
                    worry_level = item * (item if operation[2:] == 'old' else int(operation[2:]))
                else:
                    raise
                worry_level = int(worry_level/3)
                # print(f'  item={item}, worry_level={worry_level}, divisible={test_divisible_by_monkey[index]}')
                if worry_level % test_divisible_by_monkey[index] == 0:
                    # print(f'    test true: {test_true_result_by_monkey[index]}')
                    items_by_monkey[test_true_result_by_monkey[index]].append(worry_level)
                else:
                    # print(f'    test false: {test_false_result_by_monkey[index]}')
                    items_by_monkey[test_false_result_by_monkey[index]].append(worry_level)

            # print(f'after monkey {index}, {items_by_monkey}')
        # print(f'after round {round + 1}, {items_by_monkey}')

    # print(inspected_count_by_monkey)

    inspected_count_by_monkey_sorted = sorted(list(inspected_count_by_monkey.values()), reverse=True)
    # print(inspected_count_by_monkey_sorted)

    print(f'Part One: {inspected_count_by_monkey_sorted[0] * inspected_count_by_monkey_sorted[1]}')

main()