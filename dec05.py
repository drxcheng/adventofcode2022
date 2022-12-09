from copy import deepcopy

INPUT = '''                    [L]     [H] [W]
                [J] [Z] [J] [Q] [Q]
[S]             [M] [C] [T] [F] [B]
[P]     [H]     [B] [D] [G] [B] [P]
[W]     [L] [D] [D] [J] [W] [T] [C]
[N] [T] [R] [T] [T] [T] [M] [M] [G]
[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
 1   2   3   4   5   6   7   8   9

move 1 from 3 to 5
move 2 from 2 to 8
move 4 from 1 to 3
move 2 from 1 to 4
move 1 from 7 to 1
move 2 from 9 to 7
move 4 from 5 to 9
move 7 from 8 to 9
move 2 from 5 to 2
move 1 from 2 to 9
move 1 from 1 to 8
move 1 from 2 to 7
move 3 from 8 to 2
move 6 from 9 to 7
move 5 from 4 to 1
move 7 from 9 to 5
move 1 from 4 to 5
move 4 from 1 to 7
move 1 from 8 to 1
move 4 from 7 to 9
move 1 from 5 to 8
move 9 from 9 to 3
move 1 from 8 to 9
move 1 from 1 to 5
move 4 from 3 to 2
move 10 from 5 to 3
move 8 from 2 to 8
move 7 from 8 to 3
move 9 from 7 to 5
move 1 from 9 to 3
move 3 from 6 to 4
move 3 from 7 to 6
move 1 from 8 to 7
move 1 from 1 to 8
move 1 from 4 to 7
move 5 from 7 to 6
move 14 from 3 to 7
move 16 from 3 to 9
move 1 from 8 to 4
move 2 from 4 to 9
move 1 from 3 to 7
move 1 from 6 to 8
move 15 from 7 to 2
move 10 from 9 to 7
move 7 from 2 to 4
move 1 from 2 to 7
move 11 from 6 to 7
move 5 from 5 to 9
move 15 from 7 to 8
move 1 from 7 to 2
move 2 from 9 to 7
move 4 from 5 to 1
move 5 from 4 to 9
move 6 from 2 to 4
move 2 from 2 to 5
move 2 from 1 to 4
move 1 from 1 to 5
move 3 from 5 to 6
move 8 from 7 to 9
move 9 from 4 to 9
move 1 from 4 to 8
move 11 from 9 to 7
move 4 from 6 to 1
move 17 from 8 to 7
move 26 from 7 to 1
move 1 from 4 to 8
move 24 from 1 to 7
move 22 from 9 to 3
move 1 from 8 to 2
move 6 from 3 to 4
move 2 from 1 to 2
move 1 from 7 to 9
move 16 from 7 to 3
move 1 from 9 to 5
move 6 from 4 to 1
move 1 from 2 to 7
move 6 from 3 to 2
move 1 from 5 to 4
move 6 from 3 to 5
move 1 from 4 to 1
move 3 from 1 to 4
move 4 from 5 to 4
move 7 from 1 to 7
move 6 from 4 to 3
move 1 from 1 to 6
move 1 from 2 to 5
move 1 from 1 to 7
move 15 from 3 to 1
move 2 from 2 to 7
move 3 from 5 to 8
move 9 from 7 to 5
move 8 from 5 to 7
move 3 from 8 to 5
move 1 from 6 to 9
move 5 from 7 to 8
move 3 from 2 to 4
move 2 from 2 to 5
move 4 from 3 to 7
move 5 from 8 to 3
move 1 from 5 to 8
move 5 from 3 to 1
move 2 from 5 to 7
move 1 from 9 to 8
move 1 from 5 to 8
move 19 from 1 to 4
move 19 from 7 to 1
move 7 from 1 to 4
move 1 from 7 to 4
move 3 from 3 to 5
move 22 from 4 to 5
move 3 from 8 to 3
move 7 from 1 to 8
move 3 from 3 to 5
move 3 from 3 to 6
move 3 from 6 to 9
move 3 from 9 to 1
move 1 from 3 to 4
move 2 from 8 to 9
move 25 from 5 to 6
move 4 from 1 to 5
move 5 from 5 to 4
move 2 from 8 to 2
move 1 from 9 to 2
move 3 from 5 to 7
move 12 from 6 to 8
move 1 from 7 to 3
move 7 from 8 to 1
move 1 from 5 to 7
move 1 from 3 to 8
move 2 from 7 to 4
move 6 from 8 to 5
move 10 from 6 to 3
move 2 from 6 to 2
move 1 from 6 to 3
move 17 from 4 to 6
move 3 from 3 to 9
move 3 from 8 to 4
move 1 from 7 to 5
move 1 from 3 to 8
move 1 from 2 to 5
move 10 from 1 to 7
move 3 from 2 to 7
move 2 from 1 to 8
move 15 from 6 to 3
move 7 from 5 to 9
move 9 from 9 to 5
move 1 from 9 to 3
move 2 from 3 to 5
move 3 from 8 to 6
move 1 from 9 to 3
move 11 from 5 to 8
move 9 from 3 to 8
move 1 from 5 to 6
move 9 from 8 to 5
move 10 from 7 to 5
move 5 from 5 to 3
move 4 from 6 to 8
move 2 from 6 to 8
move 2 from 5 to 6
move 1 from 2 to 1
move 9 from 5 to 3
move 2 from 7 to 5
move 3 from 5 to 4
move 1 from 4 to 1
move 2 from 4 to 3
move 1 from 7 to 1
move 2 from 1 to 7
move 3 from 4 to 5
move 2 from 7 to 3
move 14 from 3 to 9
move 13 from 3 to 1
move 8 from 1 to 4
move 6 from 1 to 2
move 11 from 8 to 6
move 4 from 3 to 9
move 2 from 9 to 2
move 1 from 5 to 2
move 6 from 4 to 9
move 6 from 8 to 9
move 6 from 9 to 4
move 2 from 4 to 7
move 4 from 4 to 6
move 4 from 2 to 9
move 2 from 7 to 9
move 2 from 2 to 1
move 3 from 5 to 3
move 2 from 1 to 7
move 1 from 5 to 2
move 7 from 9 to 7
move 2 from 2 to 8
move 10 from 6 to 5
move 5 from 5 to 6
move 9 from 7 to 8
move 3 from 3 to 9
move 4 from 5 to 1
move 10 from 9 to 3
move 7 from 6 to 2
move 5 from 3 to 9
move 3 from 1 to 7
move 1 from 4 to 7
move 1 from 4 to 9
move 1 from 3 to 7
move 1 from 2 to 1
move 1 from 5 to 1
move 1 from 1 to 7
move 3 from 6 to 3
move 3 from 3 to 4
move 6 from 7 to 4
move 3 from 9 to 8
move 9 from 8 to 1
move 3 from 8 to 1
move 13 from 9 to 5
move 2 from 2 to 8
move 4 from 8 to 3
move 11 from 1 to 2
move 14 from 2 to 6
move 6 from 3 to 8
move 4 from 9 to 7
move 10 from 5 to 3
move 2 from 7 to 3
move 1 from 1 to 8
move 1 from 1 to 7
move 1 from 7 to 8
move 1 from 1 to 4
move 8 from 4 to 2
move 2 from 5 to 1
move 1 from 1 to 9
move 1 from 7 to 3
move 1 from 9 to 5
move 1 from 4 to 2
move 1 from 4 to 6
move 1 from 7 to 3
move 11 from 6 to 9
move 4 from 2 to 5
move 4 from 2 to 5
move 10 from 5 to 6
move 9 from 9 to 5
move 1 from 9 to 2
move 2 from 8 to 4
move 1 from 9 to 6
move 5 from 2 to 1
move 5 from 8 to 6
move 4 from 1 to 9
move 1 from 8 to 1
move 3 from 9 to 4
move 5 from 5 to 1
move 1 from 9 to 7
move 11 from 6 to 3
move 4 from 4 to 9
move 9 from 6 to 5
move 2 from 6 to 5
move 3 from 9 to 1
move 1 from 4 to 8
move 4 from 1 to 3
move 3 from 5 to 4
move 2 from 4 to 9
move 2 from 9 to 4
move 1 from 9 to 8
move 6 from 5 to 4
move 1 from 7 to 8
move 3 from 5 to 2
move 3 from 8 to 5
move 1 from 2 to 1
move 24 from 3 to 9
move 2 from 2 to 1
move 10 from 1 to 7
move 18 from 9 to 8
move 5 from 3 to 7
move 5 from 9 to 5
move 12 from 7 to 2
move 1 from 7 to 6
move 8 from 4 to 7
move 1 from 4 to 5
move 12 from 5 to 9
move 1 from 6 to 9
move 3 from 2 to 8
move 5 from 7 to 3
move 21 from 8 to 7
move 3 from 3 to 8
move 11 from 9 to 5
move 10 from 5 to 6
move 3 from 7 to 2
move 3 from 6 to 4
move 2 from 3 to 1
move 2 from 3 to 5
move 1 from 1 to 7
move 1 from 1 to 4
move 3 from 4 to 1
move 1 from 9 to 1
move 1 from 4 to 3
move 3 from 5 to 8
move 1 from 9 to 6
move 4 from 2 to 3
move 6 from 8 to 6
move 1 from 9 to 3
move 7 from 2 to 4
move 5 from 4 to 5
move 1 from 2 to 6
move 3 from 1 to 9
move 3 from 9 to 4
move 1 from 1 to 9
move 2 from 5 to 3
move 3 from 5 to 2
move 4 from 7 to 2
move 2 from 4 to 3
move 2 from 2 to 3
move 2 from 4 to 8
move 5 from 2 to 3
move 6 from 6 to 4
move 8 from 7 to 3
move 4 from 4 to 5
move 1 from 3 to 1
move 2 from 8 to 6
move 7 from 7 to 5
move 1 from 9 to 1
move 14 from 3 to 6
move 4 from 7 to 1
move 6 from 5 to 3
move 4 from 1 to 2
move 9 from 3 to 5
move 1 from 7 to 2
move 2 from 3 to 7
move 1 from 4 to 8
move 1 from 4 to 9
move 3 from 3 to 6
move 9 from 5 to 2
move 1 from 8 to 9
move 1 from 1 to 7
move 1 from 9 to 3
move 1 from 4 to 8
move 1 from 9 to 4
move 3 from 5 to 1
move 2 from 1 to 9
move 1 from 4 to 9
move 15 from 6 to 9
move 3 from 3 to 5
move 2 from 1 to 3
move 2 from 7 to 4
move 5 from 6 to 5
move 6 from 2 to 9
move 1 from 7 to 2
move 2 from 4 to 6
move 2 from 3 to 1
move 1 from 1 to 6
move 1 from 8 to 3
move 1 from 3 to 9
move 3 from 5 to 1
move 3 from 6 to 2
move 6 from 5 to 3
move 6 from 6 to 8
move 4 from 1 to 6
move 12 from 9 to 7
move 4 from 6 to 8
move 1 from 5 to 1
move 2 from 8 to 2
move 2 from 2 to 1
move 5 from 3 to 6
move 3 from 1 to 6
move 5 from 8 to 6
move 1 from 3 to 6
move 5 from 2 to 7
move 8 from 9 to 4
move 15 from 7 to 8
move 5 from 6 to 3
move 1 from 3 to 8
move 15 from 8 to 3
move 7 from 2 to 9
move 1 from 7 to 4
move 10 from 9 to 5
move 4 from 6 to 4
move 3 from 8 to 6
move 1 from 8 to 6
move 1 from 7 to 3
move 10 from 6 to 9
move 7 from 3 to 2
move 10 from 9 to 7
move 8 from 5 to 7
move 8 from 3 to 7
move 1 from 5 to 9
move 1 from 6 to 8
move 1 from 5 to 4
move 1 from 8 to 6
move 5 from 3 to 8
move 9 from 4 to 2
move 1 from 9 to 2
move 4 from 2 to 3
move 2 from 2 to 9
move 2 from 4 to 8
move 4 from 9 to 1
move 1 from 4 to 9
move 1 from 7 to 8
move 9 from 2 to 1
move 1 from 2 to 5
move 1 from 5 to 3
move 1 from 9 to 3
move 4 from 3 to 6
move 4 from 8 to 9
move 2 from 3 to 6
move 2 from 6 to 9
move 1 from 4 to 8
move 3 from 6 to 3
move 2 from 6 to 5
move 1 from 5 to 2
move 2 from 2 to 1
move 9 from 7 to 3
move 7 from 3 to 9
move 9 from 9 to 8
move 10 from 7 to 1
move 3 from 9 to 3
move 3 from 3 to 1
move 5 from 8 to 3
move 1 from 9 to 3
move 1 from 5 to 6
move 3 from 8 to 4
move 1 from 8 to 4
move 2 from 8 to 2
move 7 from 3 to 8
move 4 from 4 to 2
move 1 from 4 to 6
move 1 from 8 to 1
move 5 from 7 to 5
move 2 from 6 to 7
move 3 from 8 to 7
move 2 from 2 to 1
move 23 from 1 to 6
move 2 from 3 to 5
move 1 from 3 to 6
move 1 from 7 to 2
move 22 from 6 to 4
move 5 from 2 to 7
move 6 from 5 to 3
move 17 from 4 to 1
move 5 from 8 to 2
move 23 from 1 to 7
move 5 from 3 to 1
move 15 from 7 to 2
move 2 from 3 to 4
move 1 from 8 to 4
move 5 from 1 to 9
move 6 from 7 to 1
move 8 from 4 to 6
move 4 from 9 to 5
move 3 from 5 to 7
move 1 from 9 to 1
move 7 from 7 to 4
move 7 from 1 to 5
move 10 from 2 to 3
move 4 from 2 to 4
move 6 from 2 to 8
move 7 from 6 to 7
move 7 from 3 to 1
move 3 from 6 to 2
move 5 from 8 to 7
move 7 from 5 to 7
move 1 from 5 to 6
move 1 from 6 to 2
move 2 from 3 to 4
move 1 from 3 to 7
move 1 from 2 to 6
move 3 from 7 to 6
move 1 from 8 to 3
move 4 from 4 to 2
move 2 from 4 to 9
move 2 from 1 to 7
move 1 from 4 to 9
move 1 from 3 to 5
move 4 from 6 to 1
move 3 from 4 to 5
move 2 from 4 to 1
move 8 from 7 to 1
move 1 from 4 to 1
move 6 from 2 to 3
move 1 from 2 to 4
move 4 from 3 to 2
move 1 from 4 to 5
move 3 from 2 to 5
move 11 from 7 to 5
move 2 from 9 to 1
move 8 from 7 to 4
move 2 from 3 to 5
move 1 from 2 to 1
move 8 from 4 to 1
move 1 from 9 to 4
move 7 from 5 to 4
move 22 from 1 to 5
move 5 from 4 to 2
move 6 from 1 to 7
move 4 from 2 to 7
move 19 from 5 to 4
move 1 from 7 to 6
move 3 from 1 to 6
move 3 from 7 to 9
move 1 from 2 to 4
move 20 from 4 to 6
move 13 from 5 to 9
move 2 from 1 to 3
move 10 from 9 to 8
move 3 from 9 to 4
move 1 from 8 to 1
move 1 from 1 to 8
move 1 from 3 to 1
move 2 from 9 to 2
'''

INPUT_SAMPLE = '''    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

lines = INPUT.split('\n')

item_stack = {}
item_stack_part_one = {}
item_stack_part_two = {}
for line in lines:
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
