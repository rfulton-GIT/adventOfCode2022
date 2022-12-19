fname = "input.txt"
f = open(fname)
lines = f.readlines()
f.close()
n = 0
for line in lines:
    x = line.split(',')
    left, right = sorted([[int(p) for p in el.split('-')] for el in x])
    n += right[0] <= left[1]
print(n)
