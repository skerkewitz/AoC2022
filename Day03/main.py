import functools

lines = open("real.txt", "r").read().split("\n")
#lines = open("test.txt", "r").read().split("\n")


def count_item(items):
    m = {}
    for c in items:
        if m.get(c) is None:
            m[c] = [c]
        else:
            m[c].append(c)

    return {k: len(v) for (k, v) in m.items()}


def score(c: str):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 65 + 27


# Part 1
result = 0
for line in lines:
    cut = len(line) // 2
    first, second = line[0:cut], line[cut:]

    first_count = count_item(first)
    second_count = count_item(second)

    matching_items = list(set(first_count.keys()) & set(second_count.keys()))
    matching_items_count = {k: min(first_count[k], second_count[k]) for k in matching_items}

    for (k, v) in matching_items_count.items():
        result += score(k)


print(result)

# Part 2
n = 3
elfs = [lines[i:i + n] for i in range(0, len(lines), n)]

result = 0
for elf in elfs:
    e1 = count_item(elf[0])
    e2 = count_item(elf[1])
    e3 = count_item(elf[2])

    matching_items = list(set(e1.keys()) & set(e2.keys()) & set(e3.keys()))
    result += score(matching_items[0])


print(result)
