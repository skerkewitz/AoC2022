import itertools

class Grid:

    def __init__(self, lines: [str]):
        self.max_y = len(lines)
        self.max_x = len(lines[0])
        self.grid = []
        for y, line in enumerate(lines):
            self.grid.append([])
            for x, e in enumerate(line):
                self.grid[y].append((int(e), None))

    def is_visible(self, x: int, y: int):
        if x == 0 or x == self.max_x - 1:
            return True
        if y == 0 or y == self.max_y - 1:
            return True

        t, _ = self.grid[y][x]
        if all([t > o for (o, v) in self.grid[y][0:x]]):
            return True
        if all([t > o for (o, v) in self.grid[y][x+1:self.max_x]]):
            return True
        if all([t > self.grid[j][x][0] for j in range(0, y)]):
            return True
        if all([t > self.grid[j][x][0] for j in range(y + 1, self.max_y)]):
            return True

        return False

    def score_at(self, x: int, y: int):
        t, _ = self.grid[y][x]

        #  left
        left = list(reversed([o for (o, v) in self.grid[y][0:x]]))
        left_ = itertools.takewhile(lambda e: e < t, left)
        left_count = len(list(left_))
        if left_count < len(left):
            left_count += 1

        #  right
        right = [o for (o, v) in self.grid[y][x+1:self.max_x]]
        right_ = itertools.takewhile(lambda e: e < t, right)
        right_count = len(list(right_))
        if right_count < len(right):
            right_count += 1

        #  up
        up = list(reversed([self.grid[j][x][0] for j in range(0, y)]))
        up_ = itertools.takewhile(lambda e: e < t, up)
        up_count = len(list(up_))
        if up_count < len(up):
            up_count += 1

        #  down
        down = [self.grid[j][x][0] for j in range(y + 1, self.max_y)]
        down_ = itertools.takewhile(lambda e: e < t, down)
        down_count = len(list(down_))
        if down_count < len(down):
            down_count += 1
#
        return left_count * right_count * up_count * down_count


    def check_visibility(self):
        for y in range(0, self.max_y):
            for x in range(0, self.max_x):
                self.grid[y][x] = self.grid[y][x][0], self.is_visible(x, y)

    def calc_score(self):
        max_score = 0
        for y in range(0, self.max_y):
            for x in range(0, self.max_x):
                score_at = self.score_at(x, y)
                max_score = max(max_score, score_at)

        return max_score


lines = open("real.txt", "r").read().split('\n')
grid = Grid(lines)

grid.check_visibility()
print(f'Result part 1: {len([(height, visible) for height, visible in sum(grid.grid, []) if visible])}')

print(f'Result part 2: {grid.calc_score()}')


