"""
https://adventofcode.com/2022/day/3
"""
from task_input import task_input


def value(l: str) -> int:
    v = ord(l)
    if v >= 97:
        return v - 96
    return v - 38


def split(s: str) -> tuple[str, str]:
    l = int(len(s) / 2)
    return s[:l], s[l:]


def part_1():
    c = 0
    for s in task_input:
        l, r = split(s)
        ls = set(l)
        i = ls.intersection(r)
        c += sum([value(k) for k in i])
    print(c)


def part_2():
    c = 0
    for i in range(0, len(task_input), 3):
        e1 = task_input[i]
        e2 = task_input[i + 1]
        e3 = task_input[i + 2]
        a = set(e1).intersection(e2).intersection(e3)
        c += sum([value(k) for k in a])
    print(c)


if __name__ == '__main__':
    part_1()
    part_2()
    ll = 'abcdefghijklmnopqestuvwxyz'
    ll2 = 'ABCDEFGHIJKLMNOPQESTUVWXYZ'
