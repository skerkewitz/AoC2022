import re

class DirNode:
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.files = []
        self.dirs = {}

    def add_dir(self, node):
        node.parent = self
        self.dirs[node.name] = node

    def disc_usage(self):
        files_size = sum([size for (size, name) in self.files])
        dir_size = sum([d.disc_usage() for d in self.dirs.values()])
        return files_size + dir_size

    def list_usage_smaller(self, max_size: int):
        result = []
        usage = self.disc_usage()
        if usage <= max_size:
            result.append(self)

        for d in self.dirs.values():
            result.extend(d.list_usage_smaller(max_size))

        return result

    def list_usage(self):
        result = []
        usage = self.disc_usage()
        result.append((usage, self.name))
        for d in self.dirs.values():
            result.extend(d.list_usage())

        return result


def parse_file(s: str):
    p = re.compile(r'(\d*) (.*)')
    match = p.match(s)
    return int(match.group(1)), match.group(2)


def parse_dir(s: str):
    p = re.compile(r'\$ cd (.*)')
    match = p.match(s)
    return match.group(1)


lines = open("real.txt", "r").read().split('\n')
lines.pop(0)

root = DirNode("/")
cwd = root

i = iter(lines)
while True:
    try:
        cmd = next(i)
        if cmd == '$ ls':   # ignore ls
            continue
        if cmd.startswith("dir "):  # ignore dir
            continue

        if cmd.startswith("$ cd "):
            dir_name = parse_dir(cmd)
            if dir_name == '..':
                cwd = cwd.parent
            else:
                new_dir = cwd.dirs.get(dir_name)
                if new_dir is None:
                    new_dir = DirNode(dir_name)
                    cwd.add_dir(new_dir)

                cwd = cwd.dirs[dir_name]
            continue

        file_item = parse_file(cmd)
        cwd.files.append(file_item)

    except StopIteration:
        break

print(f'Result part 1: {sum([n.disc_usage() for n in (root.list_usage_smaller(100000))])}')

available = 70000000
needed = 30000000
min_delete = needed - (available - root.disc_usage())

possible = [(size, name) for (size, name) in root.list_usage() if size > min_delete]
possible.sort(key=lambda x: x[0])

print(f'Result part 2: {possible[0][0]}')
