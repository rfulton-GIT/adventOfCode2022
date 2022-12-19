fname = "input.txt"
f = open(fname)
lines = f.readlines()
f.close
n = len(lines[0])//4

onBlocks = True
blocks = [[] for _ in range(n)]
movements = []
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

for L in lines:
    if onBlocks:
        if len(L) == 1:
            onBlocks = False
            for i in range(len(blocks)):
                stack = []
                for j in range(len(blocks[i]) - 1, -1, -1):
                    stack.append(blocks[i][j])
                blocks[i] = stack
        else:
            elements = [L[4*i + 1] for i in range(n)]
            if elements == [str(i+1) for i in range(n)]:
                continue
            else:
                for i in range(n):
                    if elements[i] == " ":
                        continue
                    else:
                        blocks[i].append(elements[i])

    else:
        words = L.split()
        # make ints out of the 2nd, 4th, and 6th words
        nums = list(map(lambda x: int(words[x]), [1,3,5]))
        tmp = []
        for _ in range(nums[0]):
            source = blocks[nums[1] - 1]
            tmp.append(source.pop())
        for _ in range(nums[0]):
            dest = blocks[nums[2] - 1]
            dest.append(tmp.pop())

print("".join([blocks[i][-1] for i in range(n)]))
        
        
        

