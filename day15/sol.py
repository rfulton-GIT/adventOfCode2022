magicRow = 10
fname = "test.txt"
fname = "input.txt"
magicRow = 2000000

f = open(fname)
lines = f.readlines()
f.close()

illegal_cols = set()
beacon_cols = set()
for line in lines:
    words = line.split()
    sx = int(words[2][words[2].index('=')+1:words[2].index(',')])
    sy = int(words[3][words[3].index('=')+1:words[3].index(':')])
    bx = int(words[8][words[8].index('=')+1:words[8].index(',')])
    by = int(words[9][words[9].index('=')+1:])
    # print(sx,sy,bx,by)
    r = abs(sx - bx) + abs(sy - by)
    y_drop = abs(sy - magicRow)
    if by == magicRow:
        beacon_cols.add(bx)
    for col in range(sx + y_drop - r, 1 + sx + r - y_drop):
        illegal_cols.add(col)
# s = ""
# for i in range(-4, 27):
#     if i in beacon_cols:
#         s += 'B'
#     elif i in illegal_cols:
#         s += '#'
#     else:
#         s += '.'
# print(beacon_cols)
# print(illegal_cols)
# print(s)
print(len(illegal_cols) - len(beacon_cols))

