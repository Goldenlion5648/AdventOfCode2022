import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

def main(a : str, inp: AdventInput=None, part2=False):
    stacks = dd(list)
    lines = inp.para[0].splitlines()

    for line in lines:
        for i in range(1, len(line), 4):
            if line[i].strip().isalpha():
                stacks[(i-1)//4 + 1].append(line[i])

    for i in stacks:
        stacks[i] = stacks[i][::-1]

    second =inp.para[1].splitlines()
    for line in second:
        amount, f, to = nums(line)
        removed = [stacks[f].pop() for _ in range(amount)]
        if part2:
            removed.reverse()
        stacks[to] += removed

    return "".join(stacks[i][-1] for i in sorted(stacks))



samp = r"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".rstrip().lstrip("\n")

if samp:
    sample_advent = AdventInput(data=samp)
    sample_answer = main(sample_advent.data,sample_advent, part2=False)
    print("sample", sample_answer)
    sample_answer = main(sample_advent.data,sample_advent, part2=True)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "d" in sys.argv:
    exit()
inp = AdventInput("input5.txt")
a = inp.data
ans(main(a, inp))
ans(main(a, inp, part2=True))