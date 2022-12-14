import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input14.txt") as f:
    real_input = f.read().strip()

def irange(start, stop, step=1):
    '''makes an intelligent range that is inclusive'''
    return range(start, stop+1, step) if start <stop else range(start, stop-1, -1 if step == 1 else step)

rangei = irange
def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    board = dd(lambda : '.')
    y_max = -inf
    for line in inp.lines:
        parts = line.split(" -> ")
        parts = [lmap(int, part.split(",")) for part in parts]
        y_max = max(y_max, max(part[1] for part in parts) + 2)
        for (x, y), (x2, y2) in zip(parts, parts[1:]):
            for i in irange(*minmax(y, y2)):
                for j in irange(*minmax(x, x2)):
                    board[i, j] = "#"

    OPEN = "."
    SAND = "O"
    if part2:
        for x in range(-10000, 10000):
            board[y_max, x] = "#"
    for i in range(30000000):
        start = (0, 500)
        y, x = start
        moved = False
        while True:
            if y > 1000 and not part2:
                return i
            if board[y + 1, x] == OPEN:
                moved = True
                y += 1
            elif board[y + 1, x - 1] == OPEN:
                moved = True
                y += 1
                x -= 1
            elif board[y + 1, x + 1] == OPEN:
                moved = True
                y += 1
                x += 1
            else:
                break
        if not moved and part2:
            return i  +1
        board[y, x] = SAND




samp = r"""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

""".lstrip("\n")

if samp and "r" not in sys.argv:
    sample_answer = main(samp)
    print("sample", sample_answer)
    sample_answer = main(samp, part2=True)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
ans(main(real_input))
ans(main(real_input, part2=True))