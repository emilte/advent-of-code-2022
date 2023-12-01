from task_input import task_input


def part_1():
    print(max([sum(elf) for elf in task_input]))


def part_2():
    print(sum(sorted([sum(elf) for elf in task_input], reverse=True)[:3]))


if __name__ == '__main__':
    part_1()
    part_2()
