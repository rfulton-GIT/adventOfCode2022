fname = "mini.txt"
fname = "test.txt"
fname = "input.txt"

f = open(fname)
points = [eval("(" + L[:-1] + ")") for L in f.readlines()]
f.close()
hashmap = set(points)
count = 0
for i in range(len(points)):
    count += 6
    p = points[i]
    count -= (p[0] + 1, p[1], p[2]) in hashmap
    count -= (p[0] - 1, p[1], p[2]) in hashmap
    count -= (p[0], p[1] + 1, p[2]) in hashmap
    count -= (p[0], p[1] - 1, p[2]) in hashmap
    count -= (p[0], p[1], p[2] + 1) in hashmap
    count -= (p[0], p[1], p[2] - 1) in hashmap

print(len(points), count)