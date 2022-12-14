import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input13.txt") as f:
    real_input = f.read().strip()

class T:
    def __init__(self, lis) -> None:
        self.lis = lis
        pass
    def __lt__(self, other : 'T'):
        print(self.lis, other)

        if type(self.lis) == type(other):
            return self.lis < other.lis
        if isinstance(self.lis, int):
            if isinstance(other, list):
                return [self.lis] < other
            return T(self.lis) < other.lis
        if isinstance(other, int):
            if isinstance(self.lis, int):
                return self.lis < other
            return self.lis < [other]
        return self.lis < other.lis
    # def __gt__(self, other):
    #     if type(other) == int:

    def __repr__(self) -> str:
        return f"T {self.lis}"
            # if isinstance(self)
    
def compare(a : str, b : str):
        if not a:
            return True
        if not b:
            return False
        if a.isnumeric() and b.isnumeric():
            if int(a) < int(b):
                return True
            if int(a) > int(b):
                return False
            return compare()
        if a[0] == "[" and b[0] == "[":
            return compare(a[1:], b[1:])
        if a[0] == "[" and b[0] != "[":
            return compare(a[1:], f"[{b[1:]}]")
        if a[0] != "[" and b[0] == "[":
            return compare(f"[{a[1:]}]", b[1:])

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0

    G = {}
    def compare(a, b):
        # print(a, b)
        if type(a) == type(b):
            if type(a) == int:
                if a < b:
                    return 1
                if a > b:
                    return 0
                return None
                
            
            if len(a) and len(b):
                for i in range(min(len(a), len(b))):
                    cur = compare(a[i], b[i])
                    if cur is not None:
                        return cur
            if len(a) == len(b):
                return None
            return len(b) > len(a)
            # return len(b) > 0
        if type(a) == int and type(b) == list:
            if len(b):
                return compare([a], b)
            return 0
        if type(a) == list and type(b) == int:
            if len(a):
                return compare(a, [b])
            return 1
    def part2_compare(a, b):
        temp = compare(a, b)
        convert = {
            None: 0,
            1: -1,
            0 : 1
        }
        return convert[temp]
        
    div1 = [[2]]
    div2 = [[6]]
    index = 1

    sorted_ = []
    for para in inp.paras:
            a, b = lines(para)
            a = eval(a)
            b = eval(b)
            sorted_.append(a)
            sorted_.append(b)
            cur = compare(a, b)
            if cur is None:
                cur = 0
            ret += cur * index
            index += 1
    from functools import cmp_to_key
    sorted_.append(div1)
    sorted_.append(div2)
    sorted_.sort(key=cmp_to_key(part2_compare))
    # printe(sorted_)
    # for i in range(len(sorted_))
    if part2:
        return (sorted_.index(div1) + 1) * (sorted_.index(div2) + 1)
    return ret


samp = r"""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]

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