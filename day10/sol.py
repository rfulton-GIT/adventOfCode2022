fname = input()

with open(fname) as f:
    x = 1
    cycles = 0
    s = ""
    while cycles < 240:
        line = f.readline()
        # print(line)
        L = line.split()
        cycles += 1
        s += "@" if abs(x-((cycles-1)%40)) < 2 else " "
        # print("CRT:", s, cycles, x)
        if cycles % 40 == 0:
            print(s)
            s = ""
        if L[0] == "addx":
            cycles += 1
            s += "@" if abs(x-(cycles-1)%40) < 2 else " "
            # print("CRT:", s, cycles, x)
            x += int(L[1])
            if cycles % 40 == 0:
                print(s)
                s = ""
k = "1234567890--=!@#$%^&*()_+"