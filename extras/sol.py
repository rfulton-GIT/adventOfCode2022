fname = input()
f = open(fname)
lines = f.readlines()
f.close()
visited = set()
visited.add((0,0))
knots = [[0,0] for _ in range(10)]
tail = [0,0]
head = [0,0]
direction = {"R":[1,0], "L": [-1,0], "U": [0,1], "D": [0,-1]}
for line in lines:
    x = line.split()
    dh = direction[x[0]]
    steps = int(x[1])
    for _ in range(steps):
        knots[0] = [knots[0][j] + dh[j] for j in range(2)]
        for i in range(9):          
            if abs(knots[i][0] - knots[i+1][0]) >= 2 or abs(knots[i][1] - knots[i+1][1]) >= 2:
                dt = [(knots[i][0] - knots[i+1][0])/max(1, abs(knots[i][0] - knots[i+1][0])), (knots[i][1] - knots[i+1][1])/max(1, abs(knots[i][1] - knots[i+1][1]))]
                knots[i+1] = [int(knots[i+1][j] + dt[j]) for j in range(2)]
        visited.add(tuple(knots[-1]))
        print(line)
        print(knots)
        print()

print(len(visited))
