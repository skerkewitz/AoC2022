line = open("real.txt", "r").readline()


def contains_duplicate(s: str):
    for (i, c) in enumerate(s):
        for x in range(i+1, len(s)):
            if c == s[x]:
                return True

    return False


def score(line: str, count: int):
    for (i, c) in enumerate(line[0:len(line)-(count-1)]):
        sstr = line[i:i+count]
        if not contains_duplicate(sstr):
            return i + count


print(f'Result part 1: {score(line, 4)}')
print(f'Result part 2: {score(line, 14)}')
