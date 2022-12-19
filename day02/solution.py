fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
score = 0
for i in range(len(lines)):
    choices = lines[i].split()
    opponent = ord(choices[0]) - ord('A')
    me = ord(choices[1]) - ord('X')
    addOn = me + 1
    if (me - opponent) % 3 == 1:
        addOn += 6
    elif (opponent - me)%3 == 0:
        addOn += 3
    score += addOn
print(score)


