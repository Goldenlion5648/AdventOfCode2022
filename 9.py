import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input9.txt") as f:
    real_input = f.read().strip()

adj9 = adj8 + [(0,0)]
adj9.sort(key=lambda x: manhat((0,0), x), reverse=True)
def dist_diag(p1, p2):
    fringe = deque([(*p1, 0)])
    seen = set()
    while fringe:
        cury, curx, steps = fringe.popleft()
        cur =(cury, curx)
        if cur in seen:
            continue
        seen.add(cur)
        if cur == p2:
            return steps
        for dy, dx in adj9:
            fringe.append((cury + dy, curx + dx, steps + 1))

def move_segments(segments, new_pos_y,new_pos_x):
    segments[-1] = (new_pos_y, new_pos_x)
    for i in range(len(segments)-2, -1, -1):
        dist = dist_diag(segments[i], segments[i+1])
        if dist > 1:
            hi_seg_y, hi_seg_x = segments[i + 1]
            lo_seg_y, lo_seg_x = segments[i]
            around1 = adj8
            if segments[i][0] != segments[i+1][0] and segments[i][1] != segments[i+1][1]:
                around2 = adj8
            else:
                around2 = adj4
            new = {(dy + hi_seg_y, dx + hi_seg_x) for dy, dx in around1} & {(dy + lo_seg_y, dx + lo_seg_x) for dy, dx in around2}

            if len(new) > 1:
                new = {(py, px) for py, px in new if py != lo_seg_y and px != lo_seg_x}
            assert len(new) == 1
            segments[i] = new.pop()

def main(a : str, segment_count=10):
    a = a.strip()
    inp = AdventInput(data=a)
    tail = set()
    x = 0
    y = 0
    tail_pos = (0, 0)
    segments = [tail_pos]*segment_count
    for line in inp.lines:
        d, amt = line.split()
        amt = int(amt)
        for i in range(amt):
            dy, dx = dirs[d]
            y += dy
            x += dx
            move_segments(segments, y, x)

            tail.add(segments[0])
            board = dd(lambda : '.')
            for ty, tx in tail:
                board[ty, tx] = "#"
    return len(tail)




samp1 = r"""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

""".lstrip("\n")

samp2 = r"""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".lstrip("\n")

if samp1:
    sample_answer = main(samp1, segment_count=2)
    print("sample", sample_answer)
    sample_answer = main(samp2, segment_count=10)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
ans(main(real_input, segment_count=2))
ans(main(real_input, segment_count=10))