fname = "input.txt"

f = open(fname)
lines = f.readlines()
for i in range(len(lines)):
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]
f.close()
newf = open("aslist", "w")
newf.write(str(lines))
newf.close()