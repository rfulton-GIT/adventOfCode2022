fname = "test.txt"
fname = "input.txt"

f = open(fname)
lines = f.readlines()
n = (len(lines)+1)//3
count = 0
def order(a, b):
    if type(a) == type(b) == int:
        return (a>b) - (a < b)
    elif type(a) == type(b) == list:
        if a == []:
            return 0 if b == [] else -1
        elif b == []:
            return 1
        else:
            firsta, firstb = a[0], b[0]
            front = order(firsta, firstb)
            if front < 0:
                return -1
            elif front == 0:
                return order(a[1:], b[1:])
            else:
                return 1
    elif type(a) == int:
        return order([a], b)
    else:
        return order(a, [b])

def lessthan(a,b):
    return order(a,b) == -1
def deepcopy(a):
    if type(a) == int:
        return a
    elif type(a) == list:
        x = []
        for el in a:
            x.append(deepcopy(el))
        return x
    else:
        throwerror = throwerror


L = [[2],[6]]
for i in range(n):
    el1 = eval(lines[3*i])
    L.append(el1)
    el2 = eval(lines[3*i+1])
    L.append(el2)

for i in range(2*n+2):
    small = i
    for j in range(i+1, 2*n+2):
        if lessthan(L[j],L[small]):
            small = j
    # print(f"{1+i}th smallest is {L[small]}")
    tmp = deepcopy(L[small])
    L[small] = deepcopy(L[i])
    L[i] = tmp
    # print(i)
    # for el in L:
    #     print(el)
    # print()
print( (L.index([2])+1)*(L.index([6])+1) )