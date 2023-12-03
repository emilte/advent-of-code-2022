"""
https://adventofcode.com/2022/day/3
"""
from task_input import task_input


def part_1(task_input: str):
    lines = task_input.strip().split('\n')
    s = 0
    for line in lines:
        e1, e2 = line.split(',')
        e11, e12 = e1.split('-')
        e21, e22 = e2.split('-')
        r1 = set(range(int(e11), int(e12) + 1))
        r2 = set(range(int(e21), int(e22) + 1))

        if r1.issubset(r2) or r2.issubset(r1):
            s += 1
    print(s)


def part_2(task_input):
    lines = task_input.strip().split('\n')
    s = 0
    for line in lines:
        e1, e2 = line.split(',')
        e11, e12 = e1.split('-')
        e21, e22 = e2.split('-')
        r1 = set(range(int(e11), int(e12) + 1))
        r2 = set(range(int(e21), int(e22) + 1))

        if r1.intersection(r2):
            s += 1
    print(s)


if __name__ == '__main__':
    part_1(task_input)
    part_2(task_input)
