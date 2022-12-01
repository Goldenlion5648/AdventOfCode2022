import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

def part1(a : str, inp: AdventInput=None, real=True):
    best = -inf
    for para in inp.paras:
        best = max(sum(nums(para)), best)
    return best

def part2(a : str, inp: AdventInput=None, real=True):
    top = []
    for para in inp.paras:
        top.append(sum(nums(para)))
    top.sort()
    return sum(top[-3:])


samp = r"""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

""".strip()

if samp:
    sample_advent = AdventInput(data=samp)
    sample_answer = part1(sample_advent.data,sample_advent, real=False)
    print("sample", sample_answer)
    sample_answer = part2(sample_advent.data,sample_advent, real=False)
    print("sample", sample_answer)
else:
    print("no sample provided")

inp = AdventInput("input1.txt")
a = inp.data
ans(part1(a, inp))
ans(part2(a, inp))