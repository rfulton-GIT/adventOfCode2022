fname = "test.txt"
fname = "input.txt"

f = open(fname)
lines = f.readlines()
f.close()

def printStuff(blocked, original):
    minRow = maxRow = 0
    minCol = maxCol = 500
    for coords in blocked:
        a,b = coords
        minCol = min(minCol, a)
        maxCol = max(maxCol, a)
        maxRow = max(maxRow, b)
    for row in range(maxRow+1):
        s = ""
        for col in range(minCol, maxCol+1):
            if (col,row) in original:
                s += "#"
            elif (col, row) in blocked:
                s += "o"
            else:
                s += "."
        print(s)

furthestDown = 0
blocked = set()
for line in lines:
    coords = [[int(x) for x in s.split(',')] for s in line.split('->')]
    current = coords[0]
    if current[1] > furthestDown:
        furthestDown = current[1]
    for i in range(1, len(coords)):
        future = coords[i]
        if future[1] > furthestDown:
            furthestDown = current[1]
        diff = [future[0] - current[0], future[1] - current[1]]
        incr = [el if el == 0 else el//abs(el) for el in diff]
        while current != future:
            blocked.add(tuple(current))
            current = [current[i] + incr[i] for i in range(2)]
        blocked.add(tuple(future))
count = 0
original = {el for el in blocked}
while True:
    loc = [500, 0]
    while tuple(loc) not in blocked and loc[1] < furthestDown:
        if (loc[0], loc[1]+1) not in blocked:
            loc[1] += 1
        elif (loc[0] - 1, loc[1]+1) not in blocked:
            loc[1] += 1
            loc[0] -= 1
        elif (loc[0] + 1, loc[1]+1) not in blocked:
            loc[0] += 1
            loc[1] += 1
        else:
            blocked.add(tuple(loc))
    if tuple(loc) in blocked:
        # print(loc, count)
        count += 1
    else:
        break
print("printing blocked stuff:")
printStuff(blocked, original)
print(count)



    
