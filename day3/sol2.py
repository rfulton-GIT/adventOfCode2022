fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
score = 0
for i in range(0,len(lines), 3):
    s0 = lines[i][:-1]
    s1 = lines[i+1][:-1]
    s2 = lines[i+2][:-1]
    first = set(list(s0))
    second = set()
    for char in s1:
        if char in first:
            second.add(char)
    for c in s2:
        if c in second:
            addOn = (ord(c) - ord('a') + 1) if ord(c) > ord('Z') else (ord(c) - ord('A') + 27)
            score += addOn
            break
print(score)


