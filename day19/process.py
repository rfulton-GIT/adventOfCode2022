fname = "answers.txt"
f = open(fname)
lines = f.readlines()
f.close()
outname = "test_data.txt"
f = open(outname, "w")

index = 0
minute = 0
robots = []
resources = [[0,0,0,0]]
rob = [0]*4
res = [0]*4
i = 0
while index < len(lines):
    l = lines[index]
    index += 1
    if l[0] == "\n":
        continue
    elif l[0] == "=":
        if index == 1:
            continue
        robots.append(rob)
        resources.append(res)
        rob = [0]*4
        res = [0]*4
        i = 0
    else:
        words = l.split()
        try:
            rob[i] = eval(words[0])
            res[i] = eval(words[-3]) if words[-2] == "open" else eval(words[-2])
            i += 1
        except:
            variable = 3
robots.append(rob)
for i in range(len(robots)):
    line = f"{i}#{robots[i]}#{resources[i]}#{res[-1]}#{24}"
    f.write(line + "\n")
f.close()
    




    




