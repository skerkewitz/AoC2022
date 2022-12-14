import re


def parse_int(s: str):
    p = re.compile(r'^(\d+).*$')
    match = p.match(s)
    group = match.group(1)
    return int(group), s[len(group)::]


def parse_list(s: str):
    result = []

    while True:
        if s[0] == '[':
            l, s = parse_list(s[1::])
            result.append(l)
            continue

        if s[0] == ']':
            return result, s[1::]

        if s[0] == ',':
            s = s[1::]
            continue

        n, s = parse_int(s)
        result.append(n)


def parse_list_string(s):
    l, s = parse_list(s[1::])
    return l


def compare_integer(l: int, r: int):
    if l < r:
        return True
    elif l > r:
        return False
    else:
        return None


def compare_packets(l, r):
    if len(l) == 0:
        if len(l) == len(r):
            return None
        else:
            return True

    for li, le in enumerate(l):
        if li > len(r) - 1:
            return False

        if type(le) is int and type(r[li]) is int:
            c = compare_integer(le, r[li])
            if c is None:
                continue
            else:
                return c
        elif type(le) is list and type(r[li]) is list:
            c = compare_packets_print(le, r[li])
            if c is None:
                continue
            else:
                return c
        else:
            first_left = le
            right_first = r[li]

            if type(first_left) is int and type(right_first) is int:
                c = compare_integer(first_left, right_first)
                if c is None:
                    continue
                else:
                    return c
            elif type(first_left) is list and type(right_first) is int:
                c = compare_packets_print(first_left, [right_first])
                if c is None:
                    continue
                else:
                    return c
            elif type(first_left) is int and type(right_first) is list:
                c = compare_packets_print([first_left], right_first)
                if c is None:
                    continue
                else:
                    return c
            elif right_first is list:
                return False

    if len(r) == len(l):
        return None

    return True


def compare_packets_print(l, r):
    c = compare_packets(l, r)
    print(f'Comparing\n{l}\n{r}\n{c}\n')
    return c


#assert not compare_packets([[[[],3],[5,[1],[8,5],10,[5,8]]],[],[1]], [[9,[4,9]]])

assert compare_packets([1,1,3,1,1], [1,1,5,1,1])  #1
assert compare_packets([[1],[2,3,4]], [[1],4])  #2

#exit()

assert not compare_packets([9], [[8, 7, 6]])  #3
assert compare_packets([[4,4],4,4], [[4,4],4,4,4])  #4
assert not compare_packets([7,7,7,7], [7,7,7])  #5
assert compare_packets([], [3])  #6
assert not compare_packets([[[]]], [[]])  #7
assert not compare_packets([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])  #8


#packet_pairs = open("real.txt", "r").read().split('\n\n')
packet_pairs = open("test.txt", "r").read().split('\n\n')


correct_index = []
for i, pair in enumerate(packet_pairs):
    left, right = pair.split("\n")

    left_list = parse_list_string(left)
    right_list = parse_list_string(right)
    print(left_list)
    print(right_list)
    correct = compare_packets(left_list, right_list)
    print(f'Pair {i+1} is in correct order: {correct}')
    if correct:
        correct_index.append(i+1)

print(f'Result part 1: {sum(correct_index)}')


def compare(x, y):
    c = compare_packets_print(x, y)
    if c is None:
        return 0
    elif c:
        return -1
    else:
        return 1


#packet_pairs = open("test.txt", "r").read().split('\n')
packet_pairs = open("real.txt", "r").read().split('\n')
packet_pairs.append('[[2]]]')
packet_pairs.append('[[6]]]')
packet_pairs = [parse_list_string(l) for l in packet_pairs if l != ""]
from functools import cmp_to_key
packet_pairs = sorted(packet_pairs, key=cmp_to_key(compare), reverse=False)

divider1 = 0
divider2 = 0
for i, e in enumerate(packet_pairs):
    if e == [[2]]:
        divider1 = i + 1

    if e == [[6]]:
        divider2 = i + 1


print(f'Result part 2: {divider1 * divider2}')



assert parse_int('2,2') == (2, ',2')
assert parse_int('32,2') == (32, ',2')

#assert parse_list_string('[32,2]') == [32, 2]
assert parse_list_string('[[1],[2,3,4]]') == [[1], [2, 3, 4]]


