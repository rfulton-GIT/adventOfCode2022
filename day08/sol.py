fname = input()
f = open(fname)

lines = f.readlines()
f.close()
heights = [[int(x) for x in line[:-1]] for line in lines]
n = len(heights)
m = len(heights[0])
visible = [[0 for _ in range(m)] for _ in range(n)]
print(f"{n} rows and { m} columns")
#vertical scans
for col in range(m):
	tallestSeen = -1
	row = 0
	while tallestSeen < 9 and row < n:
		if heights[row][col] > tallestSeen:
			visible[row][col] = 1
			tallestSeen = heights[row][col]
		row += 1
	tallestSeen = -1
	row = n-1
	while tallestSeen < 9 and row > -1:
		if heights[row][col] > tallestSeen:
			visible[row][col] = 1
			tallestSeen = heights[row][col]
		row -= 1
#lateral scans
for row in range(n):
	tallestSeen = -1
	col = 0
	while tallestSeen < 9 and col < m:
		if heights[row][col] > tallestSeen:
			visible[row][col] = 1
			tallestSeen = heights[row][col]
		col += 1
	tallestSeen = -1
	col = m-1
	while tallestSeen < 9 and col > -1:
		if heights[row][col] > tallestSeen:
			visible[row][col] = 1
			tallestSeen = heights[row][col]
		col -= 1
print(sum([sum(x) for x in visible]))
