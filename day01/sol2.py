fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
q = []
current = 0
for i in range(len(lines)):
    if lines[i] == "\n":
        q.append(current)
        current = 0
    else:
        current += int(lines[i])
q.append(current)
q.sort()
print(q[-3:])
print(sum(q[-3:]))
