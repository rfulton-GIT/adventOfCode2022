import time

fname = "mini.txt"
fname = "test.txt"
fname = "input.txt"
f = open(fname)
lines = f.readlines()
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
    def reduce_graph(self):
        # print("reducing graph")
        zerokeys = set()
        for key in self.nodes:
            n = self.nodes[key]
            if key == "AA":
                continue
            elif n.fr == 0:
                zerokeys.add(key)
        for key in zerokeys:
            n = self.nodes[key]
            self.nodes.pop(key)
            for name1 in n.adj:
                n1 = self.nodes[name1]
                for name2 in n.adj:
                    if name2 == name1:
                        continue
                    n2 = self.nodes[name2]
                    direct = n1.adj[name2] if name2 in n1.adj else float('inf')
                    indirect = n.adj[name1] + n.adj[name2]
                    if indirect < direct:
                        n1.adj[name2] = indirect
                        n2.adj[name1] = indirect

                n1.adj.pop(key) # remove all traces of the null key
    def __len__(self):
        return len(self.nodes)    

g = Graph()
for line in lines:
    words = line.split()
    name = words[1]
    rate = int(words[4][words[4].index('=') + 1:-1])
    neighbors = {}
    for i in range(9, len(words)):
        neighbors[words[i][:2]] = 1
    g.addNode(Node(name, rate, neighbors))


"""
What defines a state?
1. the time elapsed
2. the current position
3. which nodes have been switched on
"""
time_limit = 30



print("REDUCED:")
t1 = time.time()
g.reduce_graph()

ordering = list(g.nodes.keys()) # fix an ordering
L = len(g)
subsets = 2**len(g)
net_pressure = [sum([g.nodes[ordering[j]].fr*((i>>j) % 2) for j in range(L)]) for i in range(2**L)]
DP = [[[0 for position in range(len(g))] for config in range(subsets) ] for minute in range(time_limit + 1)]
# it must be backwards for optimality
# this takes 30*L*(2**L)
for minute in range(time_limit - 1, -1,-1):
    print(minute)
    for config in range(subsets):
        for position in range(len(g)):
            initial_benefit = net_pressure[config]
            node = g.nodes[ordering[position]]
            isOff = (config >>position) % 2 == 0
            turnOn = DP[minute+1][config + isOff*2**position][position]
            best = turnOn + initial_benefit
            for name in node.adj:
                new_pos = ordering.index(name)
                travel_time = node.adj[name]
                if travel_time + minute > time_limit:
                    best = max(best, initial_benefit)
                else:
                    alt = travel_time*initial_benefit 
                    alt += DP[minute + travel_time][config][new_pos]
                    best = max(best, alt)
            DP[minute][config][position] = best
t2 = time.time()
deltat = t2 - t1
print(g)
print(DP[0][0][ordering.index("AA")])
print(f"{time_limit*subsets*len(g)} steps took {deltat} seconds")


    


