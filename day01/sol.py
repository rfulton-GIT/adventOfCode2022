fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
biggest = 0
current = 0
for i in range(len(lines)):
    if lines[i] == "\n":
        biggest = max(biggest, current)
        current = 0
    else:
        current += int(lines[i])
print(max(biggest, current))


