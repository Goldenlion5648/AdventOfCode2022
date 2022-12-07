import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input7.txt") as f:
    real_input = f.read().strip()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    node = lambda : dd(node)
    G = node()
    cur = G
    pos = 0
    total_sizes = dd(int)
    def get_size(cur, full_path):
        for option in cur:
            if type(cur[option]) == int:
                total_sizes[full_path] += cur[option]
            else:
                get_size(cur[option], f"{full_path}/{option}")
                total_sizes[full_path] += total_sizes[f"{full_path}/{option}"]

    path = []
    while pos < len(inp.lines):
        line = inp.lines[pos]
        parts = line.split()
        if parts[0].isnumeric():
            path.append(parts[-1])
            cur[path[-1]] = int(parts[0])
            path.pop()
        elif "$ cd" in line:
            if line.endswith(".."):
                path.pop()
                cur = G
                for x in path:
                    cur = cur[x]
            elif line.endswith("/"):
                path = ["/"]
                cur = G["/"]
            else:
                cur = cur[(parts[-1])]
                path.append(parts[-1])
            
        elif "$ ls" in line:
            pos += 1
            while pos + 1 < len(inp.lines) and "$" not in inp.lines[pos]:

                parts = inp.lines[pos].split()
                if parts[0].isnumeric():
                    path.append(parts[-1])
                    cur[path[-1]] = int(parts[0])
                    path.pop()
                
                pos += 1
            continue
        pos += 1
    get_size(G, "")
    total_sizes.pop("")
    if part2:
        space = 70000000 - total_sizes["//"]
        return min(v for v in total_sizes.values() if space + v >= 30000000)
    return sum(v for v in total_sizes.values() if v <= 100000)

            




samp = r"""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".lstrip("\n")

if samp:
    sample_answer = main(samp, part2=False)
    print("sample", sample_answer)
    sample_answer = main(samp, part2=True)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
ans(main(real_input, part2=False))
ans(main(real_input, part2=True))