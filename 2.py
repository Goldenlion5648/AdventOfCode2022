import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

def part1(a : str, inp: AdventInput=None, real=True):
    a = a.strip()
    return sum(get_score(*line.split()) for line in inp.lines)

def part2(a : str, inp: AdventInput=None, real=True):
    a = a.strip()
    options = "ABC"
    ret = 0
    for line in inp.lines:
        a, b = line.split()
        op_pos = options.index(a)
        if b == "X":
            me = options[(op_pos + 2) % 3]
        elif b == "Y":
            me = a
        else:
            me = options[(op_pos + 1) % 3]
        ret += get_score(a, me)
    return ret

def standardize(s):
    type1 = "ABC"
    type2 = "XYZ"
    if s not in type2:
        return s
    return type1[type2.index(s)]
    
def get_score(opponent, me):
    options = "ABC"
    me = standardize(me)
    score_from_option = options.index(me) + 1
    score_from_outcome = None
    me_pos = options.index(me)
    op_pos = options.index(opponent)
    assert me_pos >= 0
    assert op_pos >= 0
    
    if me_pos == op_pos:
        score_from_outcome = 3
    elif me_pos == (op_pos + 1) % len(options):
        score_from_outcome = 6
    else:
        score_from_outcome = 0
    return score_from_outcome + score_from_option




samp = r"""
A Y
B X
C Z

""".strip()

if samp:
    sample_advent = AdventInput(data=samp)
    sample_answer = part1(sample_advent.data,sample_advent, real=False)
    print("sample", sample_answer)
    sample_answer = part2(sample_advent.data,sample_advent, real=False)
    print("sample", sample_answer)
else:
    print("no sample provided")

inp = AdventInput("input2.txt")
a = inp.data
ans(part1(a, inp))
ans(part2(a, inp))