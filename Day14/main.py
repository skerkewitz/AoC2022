lines = open("real.txt", "r").read().split('\n')


def convert_coords(s: str):
    parts = s.split(',')
    return int(parts[0]), int(parts[1])


def parse_coords(l: str):
    return [convert_coords(c) for c in l.split(' -> ')]


field = {}
def draw_segments(seg: list):
    cur = seg[0]
    remaining = seg[1::]

    field[cur] = '#'
    for n in remaining:
        while cur != n:
            x, y = cur
            if x > n[0]:
                x -= 1
            elif x < n[0]:
                x += 1
            if y > n[1]:
                y -= 1
            elif y < n[1]:
                y += 1

            cur = (x,y)
            field[cur] = '#'

        cur = n


lines = [parse_coords(l) for l in lines]
for l in lines:
    draw_segments(l)


min_x, min_y = 500, 0
max_x, max_y = 500, 0

for k in field.keys():
    x, y = k
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

field_reset = field.copy()


def simulate_unit(x, y):
    while True:
        if y > max_y:
            return True

        c = field.get((x, y + 1))
        if c is None:
            y += 1
            continue

        c = field.get((x - 1, y + 1))
        if c is None:
            y += 1
            x -= 1
            continue

        c = field.get((x + 1, y + 1))
        if c is None:
            y += 1
            x += 1
            continue

        field[(x, y)] = 'o'
        return False


def simulate_unit2(x, y):
    c = field.get((x, y))
    if c == 'o':
        return True

    while True:
        if y < max_y + 1:
            c = field.get((x, y + 1))
            if c is None:
                y += 1
                continue

            c = field.get((x - 1, y + 1))
            if c is None:
                y += 1
                x -= 1
                continue

            c = field.get((x + 1, y + 1))
            if c is None:
                y += 1
                x += 1
                continue

        field[(x, y)] = 'o'
        return False


i = 0
while not simulate_unit(500, 0):
    i += 1

print(f'Result part 1: {i}')

field = field_reset
i = 0
while not simulate_unit2(500, 0):
    i += 1

print(f'Result part 2: {i}')





