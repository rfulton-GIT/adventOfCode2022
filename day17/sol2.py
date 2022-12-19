import time
t1 = time.time()
fname = "test.txt"
# fname = "input.txt"

f = open(fname)
JETS = f.readline()[:-1]
f.close()
ROCKS = [ [[True]*4], [[abs(i-1) + abs(j-1) <= 1 for j in range(3)] for i in range(3)],[[max(i,j) == 2 for j in range(3)] for i in range(3)],[[True]]*4,[[True]*2]*2]


num_rocks = 100000
max_height = max([len(r) for r in ROCKS])
height_bound = num_rocks*max_height
chamber = [[0 for _ in range(7)] for _ in range(height_bound)]
answers = []
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
    answers.append(tower_height)
solution = answers[-1]
print(solution)
t2 = time.time()
print(f"part 1 took {round(t2 - t1,1)} sec")
"""
we want to predict the height of the tower after 1 trillion rocks are added, i.e.,
the hypothetical value of answers[999999999999].In order to do this, we would like to establish
periodicity of the derivatives.
"""

increment = [answers[i] - (0 if i == 0 else  answers[i-1]) for i in range(num_rocks)]
count = 0
phase = None
freq = None
for offset in range(1000):
    for period in range(1,10000):
        isValid = True
        for i in range(offset, num_rocks - period):
            if increment[i] != increment[i+period]:
                isValid = False
                break
        if isValid:
            print(f"starting at rock {offset}, increments are periodic with period {period} rocks")
            phase = offset
            freq = period
            count += 1
            break
    if count > 0:
        break
t3 = time.time()
print(f"part 2 took {round(t3 - t2,1)} sec.")

target = 999999999999 + 1
after = (target - phase)%freq
print(f" What is the height after the first {target} rocks fall?")
print(f"the first {phase} rocks give height {answers[phase-1]}")
print(f"the next {freq} rocks give additional height {answers[phase+freq-1] - answers[phase-1]}")
print(f"There are {(target-phase)//freq} of these groups, and {(target-phase) % freq} rocks left over")
after = (target - phase)%freq
print(f"The {after} remaining rocks grant an additional {answers[phase-1+after] - answers[phase-1]} height")
start = answers[phase-1]
middle = (answers[phase+freq-1] - answers[phase-1])*((target-phase)//freq)
end = answers[phase-1+after] - answers[phase-1]
print(f"before period give {start}, middle gives {middle}, after gives {end}")
print(f"total is {start + middle + end}")

