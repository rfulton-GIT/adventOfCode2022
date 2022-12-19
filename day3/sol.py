fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
score = 0
for j in range(len(lines)):
    s = lines[j][:-1]
    L = len(s)
    half = L//2
    hashmap = set()
    for i in range(half):
        hashmap.add(s[i])
    c = None
    for i in range(half, L):
        if s[i] in hashmap:
            c = s[i]
            break
    try:
        addOn = (ord(c) - ord('a') + 1) if ord(c) > ord('Z') else (ord(c) - ord('A') + 27)
        score += addOn
    except:
        print(f"error line {j} (half = {half}, c = {c}): {s}")
print(score)


