import functools
import re


class Monkey:
    r_monkey_boy = re.compile(r'Monkey (\d+)')
    index = 0
    items = []
    stress = []
    operand_a = ""
    operator = ""
    operand_b = ""
    divisor = -1
    monkey_if_true = -1
    monkey_if_false = -2
    inspections = 0

    def __init__(self, monkey):
        monkey_boy = self.r_monkey_boy.findall(monkey)
        if monkey_boy:
            self.index = int(monkey_boy[0])

    def think(self, worry):
        self.inspections = self.inspections + 1
        # print(f'\tMonkey {self.index} inspects an item with a worry level of {worry}')
        my_worry = self.operate(worry)
        # part 1 uncomment:
        # my_worry = int(my_worry / 3)
        # print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {my_worry}.')
        if my_worry % self.divisor == 0:
            # print(f'\t\tCurrent worry level is divisible by {self.divisor}.')
            return True, my_worry
        else:
            # print(f'\t\tCurrent worry level is not divisible by {self.divisor}.')
            return False, my_worry

    def operate(self, worry):
        if self.operand_b == "old":
            stress = worry
        else:
            stress = int(self.operand_b)

        match self.operator:
            case "*":
                # print(f'\t\tWorry level is multiplied by {stress} to {worry * stress}.')
                return worry * stress
            case "+":
                # print(f'\t\tWorry level increases by {stress} to {worry + stress}.')
                return worry + stress
            case "/":
                return worry / stress
            case "-":
                return worry - stress


def solve():
    r_operation = re.compile(r'new = (.+) ([\*/\+-]) (.*)')
    r_test = re.compile(r'divisible by (\d+)')
    with open('day11/sample.txt', 'r') as file:
        monkeys = [Monkey(file.readline().strip())]
        for line in file:
            line = line.strip()
            if line.startswith("Monkey"):
                monkeys.append(Monkey(line))
            elif line.startswith("Starting items:"):
                monkeys[-1].items = [int(item) for item in line.replace("Starting items:", "").strip().split(",")]
                monkeys[-1].stress = []
            elif line.startswith("Operation:"):
                operation = r_operation.findall(line)
                monkeys[-1].operand_a = operation[0][0]
                monkeys[-1].operator = operation[0][1]
                monkeys[-1].operand_b = operation[0][2]
            elif line.startswith("Test"):
                test = r_test.findall(line)
                monkeys[-1].divisor = int(test[0])
            elif line.startswith("If true: throw to monkey"):
                monkeys[-1].monkey_if_true = int(line.replace("If true: throw to monkey", "").strip())
            elif line.startswith("If false: throw to monkey"):
                monkeys[-1].monkey_if_false = int(line.replace("If false: throw to monkey", "").strip())

        for index in range(0, 10000):
            for cheeky_boi in monkeys:
                # print(f'\nMonkey {cheeky_boi.index}:')
                for item in cheeky_boi.items:
                    test, worry = cheeky_boi.think(item)
                    if test:
                        # print(f'\t\tItem with worry level {worry} is thrown to monkey {cheeky_boi.monkey_if_true}.')
                        monkeys[cheeky_boi.monkey_if_true].stress.append(worry)
                        monkeys[cheeky_boi.monkey_if_true].items.append(worry)
                    else:
                        # print(f'\t\tItem with worry level {worry} is thrown to monkey {cheeky_boi.monkey_if_false}.')
                        monkeys[cheeky_boi.monkey_if_false].stress.append(worry)
                        monkeys[cheeky_boi.monkey_if_false].items.append(worry)

                cheeky_boi.items.clear()
                cheeky_boi.stress.clear()

            match index:
                case 0 | 19 | 999 | 1999 | 2999 | 3999 | 4999 | 5999 | 6999 | 7999 | 8999 | 9999:
                    print(f'== After round {index}')
                    for cheeky_boi in monkeys:
                        print(f'Monkey {cheeky_boi.index} inspected items {cheeky_boi.inspections} times')

        inspections = []
        for monkey in monkeys:
            inspections.append(monkey.inspections)

        most_inspections = list(reversed(sorted(inspections)))[:2]
        print(most_inspections)
        print(functools.reduce(lambda i1, i2: i1 * i2, most_inspections))

