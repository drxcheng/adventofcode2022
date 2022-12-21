import pprint

SAMPLE = False

ROOT = 'root'
HUMAN = 'humn'

pp = pprint.PrettyPrinter()

class Monkey:
    value = None
    value_func = None
    operator = None

    def __init__(self, parts, monkeys_by_name):
        self.name = parts[0]
        self.monkeys_by_name = monkeys_by_name
        self.monkeys_by_name[self.name] = self

        if parts[1].isdigit():
            self.value = int(parts[1])
        else:
            name1, operator, name2 = parts[1].split(' ')
            self.operator = operator
            self.value_func = [
                name1,
                name2,
                lambda x, y: x + y if operator == '+' else (
                    x - y if operator == '-' else (
                        x * y if operator == '*' else (
                            int(x / y) if operator == '/' else None
                        )
                    )
                )
            ]

    def get_value(self):
        if self.value is not None:
            return self.value
        value1 = None
        if monkey1 := self.monkeys_by_name.get(self.value_func[0]):
            value1 = monkey1.get_value()
        value2 = None
        if monkey2 := self.monkeys_by_name.get(self.value_func[1]):
            value2 = monkey2.get_value()
        if value1 is not None and value2 is not None:
            return self.value_func[2](value1, value2)
        return None

    def __str__(self):
        return f'Monkey {self.name}: value: {self.get_value()}'


with open(f"dec21{'-sample' if SAMPLE else ''}.txt") as file:
    monkeys_by_name_part_one = {}
    monkeys_by_name_part_two = {}
    part_two_monkey1_name = None
    part_two_monkey2_name = None

    for line in file:
        parts = line.rstrip().split(': ')
        Monkey(parts, monkeys_by_name_part_one)

        if parts[0] == ROOT:
            part_two_monkey1_name, _, part_two_monkey2_name = parts[1].split(' ')
            continue
        elif parts[0] == HUMAN:
            continue

        Monkey(parts, monkeys_by_name_part_two)

    print(f'Part One: {monkeys_by_name_part_one[ROOT].get_value()}')

    # for monkey in monkeys_by_name_part_two.values():
    #     print(monkey)

    monkey1 = monkeys_by_name_part_two[part_two_monkey1_name]
    monkey2 = monkeys_by_name_part_two[part_two_monkey2_name]

    result = monkey2.get_value()
    monkey = monkey1
    human_dependencies = []
    while True:
        human_dependencies.append(monkey)
        # print(f'explore {monkey.name}')
        monkey1_name, monkey2_name, _ = monkey.value_func
        monkey1 = monkeys_by_name_part_two.get(monkey1_name)
        monkey2 = monkeys_by_name_part_two.get(monkey2_name)
        # print(f'{monkey.name}: {monkey1_name} ({monkey1.get_value()}), {monkey2_name} ({monkey2.get_value()})')

        if monkey1 and monkey1.get_value() is not None:
            # print(f'{monkey1.get_value()} {monkey.operator} {monkey.value_func[1]} = {result}')
            if monkey.operator == '+':
                result = result - monkey1.get_value()
            elif monkey.operator == '-':
                result = monkey1.get_value() - result
            elif monkey.operator == '*':
                result = int(result / monkey1.get_value())
            elif monkey.operator == '/':
                result = int(monkey1.get_value() / result)
            else:
                raise
            if monkey2_name == HUMAN:
                print(f'Part Two: {result}')
                break
            monkey = monkey2
        elif monkey2 and monkey2.get_value() is not None:
            # print(f'{monkey.value_func[0]} {monkey.operator} {monkey2.get_value()} = {result}')
            if monkey.operator == '+':
                result = result - monkey2.get_value()
            elif monkey.operator == '-':
                result = result + monkey2.get_value()
            elif monkey.operator == '*':
                result = int(result / monkey2.get_value())
            elif monkey.operator == '/':
                result = result * monkey2.get_value()
            else:
                raise
            if monkey1_name == HUMAN:
                print(f'Part Two: {result}')
                break
            monkey = monkey1
        else:
            raise
