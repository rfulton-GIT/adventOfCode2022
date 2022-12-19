from functools import reduce

fname = "mini.txt"
fname = "test.txt"
fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
points = [eval("(" + L[:-1] + ")") for L in lines]
points = [(p[0] + 1, p[1] + 1, p[2] + 1) for p in points]
hashmap = set(points)

small = [100,100,100] # an upper bound
big = [0,0,0] # a lower bound

for i in range(len(points)):
    p = points[i]
    for j in range(3):
        if p[j] < small[j]:
            small[j] = p[j]
        if p[j] > big[j]:
            big[j] = p[j]
visited = [[[False for _ in range(big[2] + 2)] for _ in range(big[1] + 2)] for _ in range(big[0]+2)]
print(f"lower:{small}")
print(f"upper:{big}")

count = 0
queue = [[small[i]-1 for i in range(3)]]
rep = 0
while len(queue):
    rep += 1
    x,y,z = queue.pop()
    visited[x][y][z] = True
    neighbors = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
    inBounds = lambda p: reduce(lambda bool1,bool2: bool1 and bool2, [small[i] - 1 <= p[i] <= big[i] + 1 for i in range(3)])
    unvisited = lambda p: not(visited[p[0]][p[1]][p[2]])
    criteria = lambda p: inBounds(p) and unvisited(p)
    goodbors = filter(criteria, neighbors)
    for triple in goodbors:
        if triple in hashmap:
            count += 1
        else:
            queue.append(triple)
            visited[triple[0]][triple[1]][triple[2]] = True
print(f"rep:{rep}")
print(f"count:{count}")
