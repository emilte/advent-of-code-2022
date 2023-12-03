"""
https://adventofcode.com/2022/day/<x>
"""
from copy import deepcopy
from task_input import task_input, stacks


def part_1():
    stacks1 = deepcopy(stacks)
    for i in task_input:
        _, c, _, f, _, t = i.split()
        for _ in range(int(c)):
            stacks1[t].append(stacks1[f].pop())

    r = ''.join([s[-1] for s in stacks1.values()])
    print(r)


def part_2():
    stacks2 = deepcopy(stacks)
    for i in task_input:
        _, c, _, f, _, t = i.split()
        moving = stacks2[f][-int(c):]
        stacks2[f] = stacks2[f][:-int(c)]
        stacks2[t].extend(moving)

    r = ''.join([s[-1] for s in stacks2.values()])
    print(r)


if __name__ == '__main__':
    part_1()
    part_2()
