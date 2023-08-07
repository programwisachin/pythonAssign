print("Exercise:4 (input like 30,23,24,345)")
def prog_2():
    x = input()
    l = []
    for a in x.split(","):
        l.append(a)
        print(x)
    t = tuple(l)
    print(l)
    print(t)
prog_2()