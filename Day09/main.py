import re


def is_touching(h, t):
    if h == t:
        return True

    head_x, head_y = h
    tail_x, tail_y = t

    diff_x = abs(head_x - tail_x)
    diff_y = abs(head_y - tail_y)
    return diff_x < 2 and diff_y < 2


def clamp(l, h, v):
    return max(l, min(v, h))


def move_tail(h, t):
    head_x, head_y = h
    tail_x, tail_y = t

    x = clamp(-1, 1, head_x - tail_x)
    y = clamp(-1, 1, head_y - tail_y)
    return tail_x + x, tail_y + y


def move_head(h, d):
    head_x, head_y = h
    match d:
        case 'L':
            head_x -= 1
        case 'R':
            head_x += 1
        case 'U':
            head_y -= 1
        case 'D':
            head_y += 1
            pass

    return head_x, head_y


def simulate(rope_len: int, lines):
    rope = [(0,0) for i in range(0, rope_len)]
    tail_marker = {rope[-1]}
    p = re.compile(r'^([LRDU]) (\d*)$')
    for l in lines:
        match = p.match(l)
        d = match.group(1)
        steps = int(match.group(2))

        for i in range(0, steps):
            rope[0] = move_head(rope[0], d)

            for j in range(1, len(rope)):
                if not is_touching(rope[j - 1], rope[j]):
                    rope[j] = move_tail(rope[j - 1], rope[j])
                    tail_marker.add(rope[-1])

    return len(tail_marker)


lines = open("real.txt", "r").read().split('\n')
print(f'Result part 1: {simulate(2, lines)}')
print(f'Result part 1: {simulate(10, lines)}')
