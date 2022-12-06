import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input6.txt") as f:
    real_input = f.read().strip()

def main(a : str, size : int):
    a = a.strip()
    inp = AdventInput(data=a)
    for line in inp.lines:
        for i in range(len(line)):
            if len(set(line[i:i+size])) == size:
                return i + size



samp = r"""
mjqjpqmgbljsphdztnvjfqwrcgsmlb

""".lstrip("\n")

if samp:
    sample_answer = main(samp, 4)
    print("sample", sample_answer)
    sample_answer = main(samp, 14)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
ans(main(real_input, size=4))
ans(main(real_input, size=14))