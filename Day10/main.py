import itertools

lines = open("real.txt", "r").read().split('\n')

cycles = 0
register = 1

result = []
for l in lines:
    if l == 'noop':
        cycles += 1
    else:
        p = int(l.split(' ')[1])
        register += p
        cycles += 2

    print(f'Cycles {cycles} value {register}')
    result.append((cycles, register))


def register_at_cycle(l, c):
    valid = list(itertools.takewhile(lambda t: t[0] < c, l))
    if len(valid) == 0:
        return 1

    return valid[-1][1]


def signal_strength(l, c):
    return register_at_cycle(l, c) * c


print()

check_points = [20, 60, 100, 140, 180, 220]
result1: int = 0
for i in check_points:
    strength: int = signal_strength(result, i)
    print(f'Signal at {i} is {strength}')
    result1 += strength


print(f'Result part 1: {result1}')
# print(f'Result part 1: {simulate(10, lines)}')


crt: str = ''
sprite_pos = 1
for i in range(0, 240):
    sprite_pos = register_at_cycle(result, i + 1)
    crt_pos = (i % 40) + 1
    if sprite_pos <= crt_pos < sprite_pos + 3:
        crt += '#'
    else:
        crt += ' '


crt_lines = [crt[idx:idx + 40] for idx in range(0, len(crt), 40)]
for l in crt_lines:
    print(l)
