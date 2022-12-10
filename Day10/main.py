import itertools

lines = open("real.txt", "r").read().split('\n')

cycles = 0
register = 1

input_data = []
for l in lines:
    if l == 'noop':
        cycles += 1
    else:
        p = int(l.split(' ')[1])
        register += p
        cycles += 2

    input_data.append((cycles, register))


def register_at_cycle(l, c):
    valid = list(itertools.takewhile(lambda t: t[0] < c, l))
    if len(valid) == 0:
        return 1

    return valid[-1][1]


def signal_strength(l, c):
    return register_at_cycle(l, c) * c


# Part 1
check_points = [20, 60, 100, 140, 180, 220]
result1: int = 0
for i in check_points:
    strength: int = signal_strength(input_data, i)
    result1 += strength


print(f'Result part 1: {result1}')

# Part 2
crt: str = ''
sprite_pos = 1
for i in range(0, 240):
    sprite_pos = register_at_cycle(input_data, i + 1)
    crt_pos = (i % 40) + 1
    if sprite_pos <= crt_pos < sprite_pos + 3:
        crt += '#'
    else:
        crt += ' '

crt_lines = [crt[idx:idx + 40] for idx in range(0, len(crt), 40)]
print(f'Result part 2:')
for l in crt_lines:
    print(l)
