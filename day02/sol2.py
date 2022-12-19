fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()
score = 0
for i in range(len(lines)):
    choices = lines[i].split()
    opponent = ord(choices[0]) - ord('A')
    me = ord(choices[1]) - ord('Y')
    tool = (opponent + me) % 3
    addOn = tool + 1
    if choices[1] == "Z":
        addOn += 6
    elif choices[1] == "Y":
        addOn += 3
    # print(choices, addOn)
    
    score += addOn
print(score)


