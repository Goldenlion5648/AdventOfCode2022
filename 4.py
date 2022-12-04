import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

class irange:
    def __init__(self, start, stop, step=1) -> None:
        self.range = range(start, stop+1, step) if start <= stop else range(start, stop-1, -1 if step == 1 else step)
        self.start = self.range.start
        self.stop = self.range.stop
        self.step = self.range.step
    def __contains__(self, other):
        if type(other) in [range, irange]:
            return other.start in self.range and other.stop-other.step in self.range
        return other in self.range
    def overlaps(self, other):
        if type(other) in [range, irange]:
            return other.start in self.range or other.stop-other.step in self.range or\
                   self.start in other.range or self.stop-self.step in other.range
        
    def __repr__(self) -> str:
        return str(self.range)

def main(a : str, inp: AdventInput=None, real=True):
    p1 = 0
    p2 = 0
    for line in inp.lines:
        a, b = line.split(",")
        r1 = range(*nums(a,False))
        ir1 = irange(*nums(a,False))
        r2 = range(*nums(b,False))
        ir2 = irange(*nums(b,False))
        p1 += ir1 in ir2 or ir2 in ir1
        p2 += ir1.overlaps(ir2)
    return p1, p2




samp = r"""

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()

if samp:
    sample_advent = AdventInput(data=samp)
    sample_answer = main(sample_advent.data,sample_advent, real=False)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "d" in sys.argv:
    exit()
inp = AdventInput("input4.txt")
a = inp.data
ans(main(a, inp))