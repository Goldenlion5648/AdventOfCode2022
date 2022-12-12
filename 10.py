import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input10.txt") as f:
    real_input = f.read().strip()

def main(a : str, real=False, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    x = 1
    wait = 0
    to_check = []
    to_add = []
    cycle = 0
    board = dd(lambda : ".")
    width = 40
    for line in inp.lines:
        if "add" in line:
            amt = nums(line)[0]
            wait += 2
            to_add.append(amt)
        else:
            wait += 1
        while wait > 0:
            board[divmod(cycle, width)] = "#" if abs(x - (cycle % 40)) <= 1 else " "
            cycle += 1
            if cycle > 0 and (cycle - 20) % width == 0 or cycle == 20:
                to_check.append(cycle * x)
            wait -= 1
        if to_add:
            x += to_add.pop()

        assert len(to_add) == 0
    # debug(to_check)
    if part2:
        for y in range(6):
            for x in range(-1, 41):
                print(board[y, x], end='')
            print()
        return
    return sum(to_check[:6])





samp = r"""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop

""".lstrip("\n")


if samp:
    sample_answer = main(samp, real=False)
    print("sample", sample_answer)
    sample_answer = main(samp, real=False, part2=True)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
ans(main(real_input, real=True))
ans(main(real_input, part2=True, real=True))