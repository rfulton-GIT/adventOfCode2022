import time

fname = "mini.txt"
fname = "test.txt"
fname = "input.txt"
f = open(fname)
lines = f.readlines()

"""
26 minutes to execute
15 non-zero valves (state information)
2**15 valve states (32768)
50 locations you can be
50 locations the elephant can be
2,130 billion things to write (divided by 2)
1,065 million things to write
31 million things took 96 seconds
so this will take about an hour, unless you can prune the state space (or do it in c++)
SPACE ANALYSIS
an int takes 8 bytes.
1065 / 13 = 82
82 million integers to store at any given moment.
650 million bytes
650 megabytes of RAM
I have 16 GB of RAM, so we should be good.
"""

class Node:
    def __init__(self, name, rate, neighbors):
        self.name = name
        self.fr = rate
        self.adj = neighbors
class Graph:
    def __init__(self):
        self.nodes = dict()
    def addNode(self, n):
        self.nodes[n.name] = n
    def __repr__(self):
        s = ""
        for key in self.nodes:
            n = self.nodes[key]
            s += key + ": " + str(n.fr) + " ->" + "".join([" " + neighbor+f"({n.adj[neighbor]})" for neighbor in n.adj]) + "\n"
        return s
    def __len__(self):
        return len(self.nodes)

g = Graph()
valves = []
ordering = []
for line in lines:
    words = line.split()
    name = words[1]
    rate = int(words[4][words[4].index('=') + 1:-1])
    neighbors = {}
    ordering.append(name)
    if rate != 0 and name not in valves:
        valves.append(name)
    for i in range(9, len(words)):
        neighbors[words[i][:2]] = 1
    g.addNode(Node(name, rate, neighbors))

time_limit = 26
L = len(ordering)
V = len(valves)
subsets = 2**V
# net pressure stores the pressure capacity of all valve configurations
net_pressure = [sum([g.nodes[valves[j]].fr*((i>>j) % 2) for j in range(V)]) for i in range(2**V)]

print(time_limit, V, L, "->", time_limit*(2**V)*(L)*(L+1)//2)

t1 = time.time()
"""
DP[A][B][C][D] denotes the maximum pressure that can be released 
after minute A when the elephant and human are at positions C and D,
respectively, and when the valves are initialized in configuration B.
"""
arr1 = [[[0 for epos in range(hpos,L)] for hpos in range(L)] for config in range(2**V) ]
arr2 = [[[0 for epos in range(hpos,L)] for hpos in range(L)] for config in range(2**V) ]
# it must be backwards for optimality
# for test input, 26 minutes, 6 valves, 10 nodes
# for actual input, 26 minutes, 15 valves, 50 nodes
# TIME ANALYSIS
# (M)x(2^V)xLx(L+1)//2 -> 91,520 (0.88 s), or 1,086,259,200  (2.9 hrs)
# SPACE ANALYSIS
# and 2^(V+4)xL^2/2 bytes = 56kB for test, 668 Mb for input
t1 = time.time()
for minute in range(time_limit - 1, -1,-1):
    if minute % 2:
        current = arr1
        prev = arr2
    else:
        current = arr2
        prev = arr1
    t2 = time.time()
    print(minute, prev[0][ordering.index('AA')][0], t2 - t1)
    for config in range(2**V):
        benefit = net_pressure[config]
        for hpos in range(L):
            for epos in range(hpos,L):

                hOff = (ordering[hpos]) in valves and (config>>valves.index(ordering[hpos])) % 2 == 0
                hMod = 2**valves.index(ordering[hpos]) if hOff else 0
                eOff = (ordering[epos]) in valves and (config>>valves.index(ordering[epos])) % 2 == 0
                eMod = 2**valves.index(ordering[epos]) if eOff else 0
                bothMod = hMod if hMod == eMod else hMod + eMod
                wait = prev[config][hpos][epos-hpos]
                best = wait
                best = max(wait, prev[config + bothMod][hpos][epos-hpos])
                for eneighb in g.nodes[ordering[epos]].adj:
                    index = ordering.index(eneighb)
                    small,big = sorted([hpos,index])
                    best = max(best, prev[ config + hMod][small][big-small])
                for hneighb in g.nodes[ordering[hpos]].adj:
                    hn_index = ordering.index(hneighb)
                    small,big = sorted([epos,hn_index])
                    best = max(best, prev[config + eMod][small][big-small])
                    for eneighb in g.nodes[ordering[epos]].adj:
                        en_index = ordering.index(eneighb)
                        small,big = sorted([en_index,hn_index])
                        best = max(best, prev[config][small][big-small])
                current[config][hpos][epos-hpos] = benefit + best

t2 = time.time()
deltat = t2 - t1

print(f"In {time_limit} minutes, {current[0][ordering.index('AA')][0]} is optimal.")
print(f"{time_limit*subsets*L*(L+1)//2} steps took {deltat} seconds")