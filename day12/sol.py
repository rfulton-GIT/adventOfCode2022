# fname = "test.txt"
fname = "input.txt"
f = open(fname)
lines = [list(line) for line in f.readlines()]
n = len(lines)
m = len(lines[0])

def dijkstra(lines, n, m):
    start = None
    end = None
    for row in range(n):
        for col in range(m):
            if lines[row][col] == 'S':
                start = [row,col]
                lines[row][col] = 'a'
            elif lines[row][col] == 'E':
                end = [row,col]
                lines[row][col] = 'z'
    queue = [start]
    shortestPath = [[0 if [row,col] == start else float('inf') for col in range(m)] for row in range(n)]
    index = 0
    while index < len(queue):
        coords = queue[index]
        i,j = coords
        index += 1
        currentChar = lines[i][j]
        inBounds = lambda coords: 0 <= coords[0] < n and 0 <= coords[1] < m
        visited = lambda coords: shortestPath[coords[0]][coords[1]] < float('inf')
        reachable = lambda coords: ord(lines[coords[0]][coords[1]]) <= ord(lines[i][j]) + 1
        criterion = lambda x: inBounds(x) and not(visited(x)) and reachable(x)
        neighbors =  filter(criterion, [[i-1,j], [i+1,j], [i,j+1], [i,j-1]])
        for neighbor in neighbors:
            row,col = neighbor
            shortestPath[row][col] = 1 + shortestPath[i][j]
            queue.append(neighbor)
    for a in range(n):
        s = ""
        for b in range(m):
            val = shortestPath[a][b]
            s += "inf " if val == float('inf') else " "*(3-len(str(val))) + str(val) + " "
        print(s)
        print()
    return shortestPath[end[0]][end[1]]

print(dijkstra(lines,n,m))