"""
https://adventofcode.com/2022/day/6
"""
from task_input import task_input


def is_marker(s: str):
    m: dict = {}
    for l in s:
        m.setdefault(l, 0)
        m[l] += 1
    return all(k == 1 for k in m.values())


def find_marker(s: str, limit: int) -> int:
    for i in range(limit, len(s)):
        if is_marker(s[i - limit:i]):
            return i
    return -1


def part_1():
    print(find_marker(task_input, 4))


def part_2():
    print(find_marker(task_input, 14))


if __name__ == '__main__':
    part_1()
    part_2()
