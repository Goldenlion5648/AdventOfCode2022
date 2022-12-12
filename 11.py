import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *
with open("input11.txt") as f:
    real_input = f.read().strip()

monkeys :list['Monkey'] = []

class Monkey:
    def __init__(self, id, items, operation, test, true, false) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspect_count = 0
    def inspect(self, mod, part2=False):
        for item in self.items:
            cur = self.operation(item)
            if not part2:
                cur //= 3
            cur %= mod
            if self.test(cur):
                self.throw(cur, self.true)
            else:
                self.throw(cur, self.false)
            self.inspect_count += 1
        self.items.clear()

    def throw(self, item, other_pos):
        monkeys[other_pos].items.append(item)
    
    def __repr__(self) -> str:
        return f"{self.id} {self.items} {self.true} {self.false} {self.inspect_count}"


def main(a: str, part2=False):
    a = a.strip()
    monkeys.clear()
    inp = AdventInput(data=a)
    mod_nums = []
    for section in inp.para:
        lines = section.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("Monkey"):
                id_ = num(line)
            elif line.startswith("Starting"):
                items = nums(line)
            elif line.startswith("Operation"):
                _, op = line.split("= ")
                op = eval(f"lambda old : {op}")
            elif line.startswith("Test"):
                _, test = line.split(":")
                mod_nums.append(num(test))
                test = eval(f"lambda test : test {test} == 0")
            elif "true" in line:
                true = num(line)
            elif "false" in line:
                false = num(line)
        monkeys.append(Monkey(id_, items, op, test, true, false))
    
    mod = lcm(*mod_nums)
    rounds = 10000 if part2 else 20
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect(mod, part2)

    temp = (sorted(monkey.inspect_count for monkey in monkeys))
    return prod(temp[-2:])
    


samp = r"""

Monkey 0:
    Starting items: 79, 98
    Operation: new = old * 19
    Test: % 23
      If true: throw to monkey 2
      If false: throw to monkey 3

  Monkey 1:
    Starting items: 54, 65, 75, 74
    Operation: new = old + 6
    Test: % 19
      If true: throw to monkey 2
      If false: throw to monkey 0

  Monkey 2:
    Starting items: 79, 60, 97
    Operation: new = old * old
    Test: % 13
      If true: throw to monkey 1
      If false: throw to monkey 3

  Monkey 3:
    Starting items: 74
    Operation: new = old + 3
    Test: % 17
      If true: throw to monkey 0
      If false: throw to monkey 1
""".lstrip("\n")

if samp:
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
