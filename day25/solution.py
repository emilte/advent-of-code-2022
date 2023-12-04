"""
https://adventofcode.com/2022/day/25
"""
from task_input import task_input

snasu2number = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}


def snasu(n: int, s: str = '', b=0, neg=False) -> str:
    my_min = 5**(b)
    my_max = 2 * my_min
    l = sum([2 * 5**i for i in range(b)])
    cm = l + my_max
    cn = l + my_min

    if s and b < 0:
        return s

    if cm < n:
        return snasu(n=n, s=s, b=b + 1)

    if n == 0:
        return snasu(n=n, s=s + '0', b=b - 1)

    if n <= l and 0 < b:
        return snasu(n=n, s=s + '0', b=b - 1, neg=neg)

    if n <= my_min:
        new_s = '-' if neg else '1'
        s += new_s
        new_n = my_min - n
        return snasu(n=new_n, s=s, b=b - 1, neg=not neg)
    if n <= cn:
        new_s = '-' if neg else '1'
        s += new_s
        new_n = n - my_min
        return snasu(n=new_n, s=s, b=b - 1, neg=neg)

    if n <= my_max:
        new_s = '=' if neg else '2'
        s += new_s
        new_n = my_max - n
        return snasu(n=new_n, s=s, b=b - 1, neg=not neg)
    if n <= cm:
        new_s = '=' if neg else '2'
        s += new_s
        new_n = n - my_max
        return snasu(n=new_n, s=s, b=b - 1, neg=neg)

    return snasu(n=n, s=s + '1', b=b - 1)


def number(snasu: str) -> int:
    return sum([5**i * snasu2number[s] for i, s in enumerate(snasu[::-1])])


def part_1():
    s = 0
    for n in task_input:
        s += number(n)
    print(s, snasu(s))


def part_2():
    ...


if __name__ == '__main__':
    # print(snasu(113))
    # for x in range(200):
    #     r = snasu(x)
    #     n = number(r)
    #     if x != n:
    #         print(x, r, n)

    part_1()
    # part_2()
