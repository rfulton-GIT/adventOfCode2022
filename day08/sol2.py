fname = input()
f = open(fname)

lines = f.readlines()
f.close()
heights = [[int(x) for x in line[:-1]] for line in lines]
n = len(heights)
m = len(heights[0])
scenery = [[1 for _ in range(m)] for _ in range(n)]
print(f"{n} rows and { m} columns")
#vertical scans
for col in range(m):
	tallestSeen = [0]
	for row in range(n):
		while len(tallestSeen) and  heights[row][col] > heights[tallestSeen[-1]][col] :
			tallestSeen.pop()
		if len(tallestSeen):
			scenery[row][col] *= row - tallestSeen[-1]
		else:
			scenery[row][col] *= row
		tallestSeen.append(row)
	tallestSeen = [n-1]
	for row in range(n-1,-1,-1):
		while len(tallestSeen) and heights[row][col] > heights[tallestSeen[-1]][col]:
			tallestSeen.pop()
		if len(tallestSeen):
			scenery[row][col] *= tallestSeen[-1] - row
		else:
			scenery[row][col] *= n-1 - row
		tallestSeen.append(row)

#lateral scans
for row in range(n):
	tallestSeen = [0] 
	for col in range(m):
		while len(tallestSeen) and heights[row][col] > heights[row][tallestSeen[-1]]:
			tallestSeen.pop()
		if len(tallestSeen):
			scenery[row][col] *= col - tallestSeen[-1]
		else:
			scenery[row][col] *= col
		tallestSeen.append(col)


	tallestSeen = [n-1]
	for col in range(m-1,-1,-1):
		while len(tallestSeen) and heights[row][col] > heights[row][tallestSeen[-1]]:
			tallestSeen.pop()
		if len(tallestSeen):
			scenery[row][col] *= tallestSeen[-1] - col
		else:
			scenery[row][col] *= m-1-col
		tallestSeen.append(col)
print(max([max(x) for x in scenery]))
