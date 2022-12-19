from functools import reduce
# fname = "test.txt"
fname = "input.txt"
class Monkey:
    def __init__(self, lines):
        self.index = int(lines[0].split()[1][0])
        self.items = eval('[' +lines[1][lines[1].index(':')+1:] + ']')
        self.strop = lines[2][lines[2].index('=')+1:-1]
        self.op = lambda old: eval(self.strop)
        self.divby = int(lines[3].split()[-1])
        self.case1 = int(lines[4].split()[-1])
        self.case2 = int(lines[5].split()[-1])
    def __repr__(self):
        s = f"index:{self.index}, items:{self.items}, op:{self.strop}, divby:{self.divby}, case1:{self.case1}, case2:{self.case2}\n"
        return s


f = open(fname)

allines = f.readlines()
allines.append(["\n"])

n = len(allines)//7
monkeys = [Monkey(allines[7*i:7*i+7]) for i in range(n)]
inspections = [0 for _ in range(n)]
maxdiv = reduce(lambda a,b: a*b, map(lambda m: m.divby, monkeys), 1)
print(maxdiv)
for _ in range(10000):
    for i in range(n):
        m = monkeys[i]
        inspections[i] += len(m.items)
        while m.items != []:
            item = m.items.pop()
            new = m.op(item) % maxdiv
            newowner = monkeys[m.case1] if new % m.divby == 0 else monkeys[m.case2]
            newowner.items.append(new)
print(inspections)
inspections.sort(reverse=True)
print(inspections[0]*inspections[1])




