import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

from more_itertools import chunked
from string import ascii_letters as letters
def part1(inp : str):
    ret = 0
    for line in inp.splitlines():
        a, b = chunked(line, len(line) // 2)
        both = set(a) & set(b)
        common =  both.pop()
        ret += letters.index(common) + 1
    return ret

def part2(inp : str):
    ret = 0
    for group in chunked(inp.splitlines(), 3):
        a, b, c = group
        both = set(a) & set(b) & set(c)
        common =  both.pop()
        ret += letters.index(common) + 1
    return ret

def main(a : str):
    print(part1(a))
    print(part2(a))


samp = r"""

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()

if samp:
    sample_advent = AdventInput(data=samp)
    sample_answer = main(sample_advent.data)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "d" in sys.argv:
    exit()
print("hi")
inp = AdventInput("input3.txt")
a = inp.data
ans(main(a))