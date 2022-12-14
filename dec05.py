from copy import deepcopy

SAMPLE = False

with open(f"dec05{'-sample' if SAMPLE else ''}.txt") as file:
    item_stack = {}
    item_stack_part_one = {}
    item_stack_part_two = {}

    for line in file:
        line = line.rstrip()

        if line.startswith('move'):
            if not item_stack_part_one and not item_stack_part_two:
                item_stack_part_one = deepcopy(item_stack)
                item_stack_part_two = deepcopy(item_stack)
            commands = line.split(' ')
            items_to_move = int(commands[1])
            src_stack = commands[3]
            dest_stack = commands[5]

            # part one
            for i in range(items_to_move):
                item = item_stack_part_one[src_stack].pop(len(item_stack_part_one[src_stack]) - 1)
                item_stack_part_one[dest_stack].append(item)

            # part two
            tmp_items = []
            for i in range(items_to_move):
                item = item_stack_part_two[src_stack].pop(len(item_stack_part_two[src_stack]) - 1)
                tmp_items = [item] + tmp_items

            item_stack_part_two[dest_stack] += tmp_items
        else:
            for i, c in enumerate(line):
                stack_no = (i - 1) / 4
                if int(stack_no) == stack_no:
                    if c.isnumeric():
                        break
                    if c != ' ':
                        # print(f'{int(stack_no)} : {c}')
                        stack_no_str = str(int(stack_no) + 1)
                        if stack_no_str not in item_stack:
                            item_stack[stack_no_str] = []
                        item_stack[stack_no_str] = [c] + item_stack[stack_no_str]

    result_part_one = ''
    for stack_number in sorted(item_stack_part_one.keys()):
        stack = item_stack_part_one[stack_number]
        top_item = stack[len(stack) - 1]
        result_part_one += top_item

    result_part_two = ''
    for stack_number in sorted(item_stack_part_two.keys()):
        stack = item_stack_part_two[stack_number]
        top_item = stack[len(stack) - 1]
        result_part_two += top_item

    print(f'Part One: {result_part_one}')
    print(f'Part Two: {result_part_two}')
