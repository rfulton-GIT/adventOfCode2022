dimension = 20
fname = "test.txt"
fname = "input.txt"
dimension = 4000000

f = open(fname)
lines = f.readlines()
f.close()

circles = []
for line in lines:
    words = line.split()
    sx = int(words[2][words[2].index('=')+1:words[2].index(',')])
    sy = int(words[3][words[3].index('=')+1:words[3].index(':')])
    bx = int(words[8][words[8].index('=')+1:words[8].index(',')])
    by = int(words[9][words[9].index('=')+1:])
    r = abs(sx - bx) + abs(sy - by)
    circles.append([sx, sy, r])
def test(a,b,circles):
    for circle in circles:
        if abs(circle[0] -a) + abs(circle[1] - b) <= circle[2]:
            # print(circle)
            # print(a,b)
            # print(abs(circle[0] -a) + abs(circle[1] - b))
            # print(r)
            return False
    if 0 <= a <= dimension and 0 <= b <= dimension:
        print(a, b)
        return True
    else:
        return False
def search(circles):
    count = 0
    for circle in circles:
        cx, cy, r = circle
        x, y = cx, cy + r
        while y >= cy:
            res = test(x,y+1,circles)
            count += 1
            if res:
                print("all done")
                return count
            x -= 1
            y -= 1
        x += 1
        y += 1
        while x <= cx:
            res = test(x-1,y,circles)
            count += 1
            if res:
                print("all done")
                return count
            x += 1
            y -= 1
        x -= 1
        y += 1
        while y <= cy:
            res = test(x,y-1,circles)
            count += 1
            if res:
                print("all done")
                return count
            x += 1
            y += 1
        x -= 1
        y -= 1
        while x >= cx:
            res = test(x+1,y,circles)
            count += 1
            if res:
                print("all done")
                return count
            x -= 1
            y += 1
        
    

num_tests = search(circles)
print(f"num_tests: {num_tests}")
# test(14,11, circles)