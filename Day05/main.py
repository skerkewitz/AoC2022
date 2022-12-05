import re
import copy

#[stack, move_str] = open("test.txt", "r").read().split("\n\n")
[stack, move_str] = open("real.txt", "r").read().split("\n\n")

stack = [l for l in stack.split('\n')]
stack_count = stack.pop()  # drop numbers lines
stack_count = 9

stacks = [[] for i in range(0, stack_count)]
for s in stack:
    s : str = s
    for i in range(0, stack_count):
        stacks[i].append(s[1 + (i * 4)])


for i in range(0, stack_count):
    stacks[i] = [e for e in stacks[i] if e != ' ']


def parse_moves(move_string: str):
    p = re.compile(r'move (\d*) from (\d*) to (\d*)')

    moves = []
    for m in move_string.split("\n"):
        match = p.match(m)
        moves.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))

    return moves


def perform_moves_part1(moves, stacks):
    for m in moves:
        (num, source, dest) = m

        for i in range(0, num):
            stacks[dest - 1].insert(0, stacks[source - 1].pop(0))

    return stacks


def perform_moves_part2(moves, stacks):
    for m in moves:
        (num, source, dest) = m

        temp = []
        for i in range(0, num):
            temp.insert(0, stacks[source - 1].pop(0))

        for i in range(0, num):
            stacks[dest - 1].insert(0, temp.pop(0))

    return stacks


moves = parse_moves(move_str)
stack_part1 = perform_moves_part1(moves, copy.deepcopy(stacks))
stack_part2 = perform_moves_part2(moves, copy.deepcopy(stacks))

print(f'Result 1: {"".join(str(stack_part1[i][0]) for i in range(0, stack_count))}')
print(f'Result 2: {"".join(str(stack_part2[i][0]) for i in range(0, stack_count))}')


