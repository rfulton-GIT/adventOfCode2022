fname = "input.txt"
f = open(fname)
lines = f.readlines()
f.close()
window = 4
for line in lines:
	string = line
	for i in range(window, len(string)):
		substring = string[i-window:i]
		if len(set(substring)) == window:
			print(i)
			break
