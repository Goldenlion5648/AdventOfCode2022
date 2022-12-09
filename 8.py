import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input8.txt") as f:
    real_input = f.read().strip()

def main(a : str, real=True):
    a = a.strip()
    inp = AdventInput(data=a)
    board = read_grid(inp.data, True)
    Y = len(inp.lines)
    X = len(inp.lines[0])
    # print(type(board[1, 3]))
    print("in file", sys.argv)
    

    def part1():
        good = set()
        for y in range(Y):
            hi = board[y, 0]
            for x in range(X):
                if x == 0 or board[y, x] > hi:
                    good.add((y, x))
                    hi = board[y, x]
        
        for y in range(Y):
            hi = board[y, X-1]
            for x in reversed(range(X)):
                if x == X-1 or board[y, x] > hi:
                    good.add((y, x))
                    hi = board[y, x]
        
        for x in (range(X)):
            hi = board[0, x]
            for y in range(Y):
                if y == 0 or board[y, x] > hi:
                    good.add((y, x))
                    hi = board[y, x]

        for x in range(X):
            hi = board[Y-1, x]
            for y in reversed(range(Y)):
                if y == Y-1 or board[y, x] > hi:
                    good.add((y, x))
                    hi = board[y, x]
        
        return len(good)
            

    def score(starty, startx):
        mult = 0
        sides = []
        for y in reversed(range(0, starty)):
            if board[y, startx] < board[starty, startx]:
                mult += 1
            else:
                mult += 1
                break
        sides.append(mult)
        mult = 0
        for y in (range(starty + 1, Y)):
            if board[y, startx] < board[starty, startx]:
                mult += 1
            else:
                mult += 1
                break
        sides.append(mult)
        mult = 0

        for x in reversed(range(0, startx)):
            if board[starty, x] < board[starty, startx]:
                mult += 1
            else:
                mult += 1
                break
        sides.append(mult)
        mult = 0
        for x in (range(startx + 1, X)):
            if board[starty, x] < board[starty, startx]:
                mult += 1
            else:
                mult += 1
                break
        sides.append(mult)
        # print(sides)
        return prod(sides)
    
    def part2():
        return max(score(y, x) for y in range(Y) for x in range(X))


    return part1(), part2()


samp = r"""

30373
25512
65332
33549
35390
""".lstrip("\n")

if samp:
    sample_answer = main(samp, real=False)
    print("sample", *sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
p1, p2 = main(real_input, real=True)
ans(p1)
ans(p2)