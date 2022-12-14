
lines = open("test.txt", "r").read().split('\n')



map_data = []
for y, l in enumerate(lines):
    ml = map_data.append([])
    for x, c in enumerate(l):
        if c == 'S':
            start = x, y
            map_data[-1].append(ord('a'))
        elif c == 'E':
            end = x, y
            map_data[-1].append(ord('a'))
        else:
            map_data[-1].append(ord(c))


max_y = len(map_data)
max_y = len(map_data[0])

print(map_data)

def possible_moves(pos, visited):
    possible = []

    for y in range(-1, 2):
        if 0 <= y < max_y:
            for x in range(-1, 2):
                if 0 <= x < max_y:
                    if (x == 0 or y == 0) and (x != y):
                        possible.append((x, y))

    return [p for p in possible if not p in visited]


def solve(cur_pos, end_pos, visited):
    print(f'f"Start: {cur_pos}, end {end_pos}, visited: {visited}')
    if cur_pos == end_pos:
        return visited

    possible = possible_moves(cur_pos, visited)
    for p in possible:
        nx, ny = p
        cx, cy = cur_pos
        nx += cx
        ny += cy
        if map_data[ny][nx] - 1 <= map_data[cy][cx]:
            print(f'Go {nx, ny}')
            v = solve((nx, ny), end_pos, visited + [cur_pos])
            if v is not None:
                return v
        else:
            print(f'Deadend {nx, ny}')

    return None


print(solve(start, end, []))


print(possible_moves((0,0), [(1,0)]))



