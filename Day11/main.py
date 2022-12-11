import math
import re


class Monkey:

    def __init__(self, monkey_id, items, operation, operand, divisible, target_true, target_false):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.operand = operand
        self.divisible = divisible
        self.target_true = target_true
        self.target_false = target_false
        self.inspect_count = 0

    def __str__(self) -> str:
        return f'Id {self.monkey_id}, items {self.items}, operation: old {self.operation} {self.operand}, targets: divisible by {self.divisible} ? {self.target_true} : {self.target_false}, inspect count {self.inspect_count}'

    @classmethod
    def parse(cls, block: str):
        lines = block.split("\n")

        # Parse monkey id
        p = re.compile(r'^Monkey (\d*):$')
        match = p.match(lines[0])
        monkey_id = match.group(1)

        # Parse starting items
        p = re.compile(r'^  Starting items: (.*)$')
        match = p.match(lines[1])
        starting_items = [int(e) for e in match.group(1).split(',')]

        # Parse Operation
        p = re.compile(r'^  Operation: new = old (.) (.+)$')
        match = p.match(lines[2])
        operation = match.group(1)
        operand = match.group(2)

        # Parse Test
        p = re.compile(r'^  Test: divisible by (\d+)$')
        match = p.match(lines[3])
        divisible = int(match.group(1))

        # Parse throw true target
        p = re.compile(r'^    If true: throw to monkey (\d+)$')
        match = p.match(lines[4])
        throw_true_target = int(match.group(1))

        # Parse throw false target
        p = re.compile(r'^    If false: throw to monkey (\d+)$')
        match = p.match(lines[5])
        throw_false_target = int(match.group(1))

        return cls(monkey_id, starting_items, operation, operand, divisible, throw_true_target, throw_false_target)

    def inspect_item(self, item: int) -> int:
        operand_value = item
        if self.operand != 'old':
            operand_value = int(self.operand)

        match self.operation:
            case '+':
                return item + operand_value
            case '*':
                return item * operand_value
            case _:
                raise RuntimeError


    @staticmethod
    def process(monkey, monkeys, max_number):
        for item in monkey.items:
            item = monkey.inspect_item(item)
            if max_number is None:
                item = item // 3
            else:
                item = item % max_number

            if item % monkey.divisible == 0:
                monkeys[monkey.target_true].items.append(item)
            else:
                monkeys[monkey.target_false].items.append(item)

        monkey.inspect_count += len(monkey.items)
        monkey.items = []

def run(block_lines, rounds, use_max_number):
    monkeys = [Monkey.parse(l) for l in monkey_block_lines]

    max_number = None
    if use_max_number:
        max_number = math.prod([m.divisible for m in monkeys])

    for r in range(1, rounds + 1):
        for m in monkeys:
            Monkey.process(m, monkeys, max_number)

    monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
    return monkeys[0].inspect_count * monkeys[1].inspect_count


monkey_block_lines = open("real.txt", "r").read().split('\n\n')
print(f'Result part 1: {run(monkey_block_lines, 20, False)}')
print(f'Result part 2: {run(monkey_block_lines, 10000, True)}')
