import time
t1 = time.time()
fname = "test.txt"
# fname = "input.txt"

f = open(fname)
JETS = f.readline()[:-1]
f.close()
ROCKS = [ [[True]*4], [[abs(i-1) + abs(j-1) <= 1 for j in range(3)] for i in range(3)],[[max(i,j) == 2 for j in range(3)] for i in range(3)],[[True]]*4,[[True]*2]*2]


num_rocks = 2022
max_height = max([len(r) for r in ROCKS])
height_bound = num_rocks*max_height
chamber = [[0 for _ in range(7)] for _ in range(height_bound)]
def isLegal(chamber, rock, row, col):
    inBounds = 0 <= col and col + len(rock[0]) - 1 < 7 and 0 <= row - len(rock) + 1
    if not(inBounds):
        return False

    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if chamber[row-i][col+j] and rock[i][j]:
                return False
    return True

tower_height = 0
jet_length = len(JETS)
jets_index = 0
wrap = 0
for rep in range(num_rocks):
    rock_choice = rep%5
    r = ROCKS[rock_choice]
    h = len(r)

    row = tower_height + 3 + h - 1
    col = 2

    while True:

        col_shift = 1 if JETS[jets_index] == ">" else -1
        prev = jets_index
        jets_index = (jets_index + 1) % jet_length
        if isLegal(chamber, r, row, col + col_shift):
            col += col_shift

        if isLegal(chamber, r, row - 1, col):
            row -= 1
        else:
            for i in range(len(r)):
                for j in range(len(r[i])):
                    chamber[row-i][col+j] = max(chamber[row-i][col+j], r[i][j])
                    if r[i][j]:
                        tower_height = max(tower_height, row-i+1)
            break
print(tower_height)