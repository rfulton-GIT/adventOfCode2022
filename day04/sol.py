fname = "input.txt"
f = open(fname)
lines = f.readlines()
f.close()
n = 0
for line in lines:
	nums = sum([[int(x) for x in el.split('-')] for el in line.split(',')], [])
	if (nums[0] <= nums[2] and nums[3] <= nums[1]) or (nums[2] <= nums[0] and nums[1] <= nums[3]):
		n += 1
print(n)
