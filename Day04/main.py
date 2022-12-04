lines = open("real.txt", "r").read().split("\n")
#lines = open("test.txt", "r").read().split("\n")


def is_inrange(x, a, b):
    return a <= x <= b


result_part1 = 0
result_part2 = 0
for line in lines:
    elf_pair = line.split(',')
    [a, b] = [int(x) for x in elf_pair[0].split('-')]
    [x, y] = [int(x) for x in elf_pair[1].split('-')]

    if (a <= x and b >= y) or (x <= a and y >= b):
        result_part1 += 1

    if is_inrange(a, x, y) or is_inrange(b, x, y) or is_inrange(x, a, b) or is_inrange(y, a, b):
        result_part2 += 1

print(f'Result Part 1: {result_part1}')
print(f'Result Part 2: {result_part2}')

