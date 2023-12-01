from task_input import task_input, ROCK, PAPER, SCISSOR, LOSE, DRAW, WIN

# A,X = Rock = 1p
# B,Y = Paper = 2p
# C,Z = Scissor = 3p
ROCKp = 1
PAPERp = 2
SCISSORp = 3

W = 6
L = 0
D = 3

game = {
    (ROCK, ROCK): D + ROCKp,
    (ROCK, PAPER): W + PAPERp,
    (ROCK, SCISSOR): L + SCISSORp,
    (PAPER, ROCK): L + ROCKp,
    (PAPER, PAPER): D + PAPERp,
    (PAPER, SCISSOR): W + SCISSORp,
    (SCISSOR, ROCK): W + ROCKp,
    (SCISSOR, PAPER): L + PAPERp,
    (SCISSOR, SCISSOR): D + SCISSORp,
}

game_2 = {
    (ROCK, LOSE): SCISSORp + L,
    (ROCK, DRAW): ROCKp + D,
    (ROCK, WIN): PAPERp + W,
    (PAPER, LOSE): ROCKp + L,
    (PAPER, DRAW): PAPERp + D,
    (PAPER, WIN): SCISSORp + W,
    (SCISSOR, LOSE): PAPERp + L,
    (SCISSOR, DRAW): SCISSORp + D,
    (SCISSOR, WIN): ROCKp + W,
}


def part_1():
    print(sum([game[g] for g in task_input]))


def part_2():
    print(sum([game_2[g] for g in task_input]))


if __name__ == '__main__':
    part_1()
    part_2()
