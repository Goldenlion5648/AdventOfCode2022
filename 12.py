import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input12.txt") as f:
    real_input = f.read().strip()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    board, starty, startx, endy, endx = read_board(a, "S", "E", "#", True)

    new_end = 'z'
    board[starty, startx] = 'a'
    board[endy, endx] = new_end
    
    def bfs(board, starty, startx, endy, endx):
        fringe = deque([(starty, startx, 0)])
        seen = {}
        while fringe:
            y, x, steps = fringe.popleft()
            cur = (y, x)
            if cur in seen:
                continue
            seen[cur] = steps
            if cur == (endy, endx):
                return steps            

            for dy, dx in adj4:
                newy = dy + y
                newx = dx + x
                if newy in range(len(inp.lines)) and newx in range(len(inp.lines[0])) and ord(board[newy, newx]) <= ord(board[y, x]) + 1:
                    fringe.append((newy, newx, steps + 1))

    if not part2:
        return bfs(board, starty, startx, endy, endx)

    ret = inf
    for y, x in board:
        if board[y, x] == 'a':
            cur = bfs(board, y, x, endy, endx)
            if cur is not None:
                ret = min(ret, cur)
    return ret



samp = r"""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

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