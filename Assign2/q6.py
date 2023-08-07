
def two_dimens_arr(x, y):
    l1 = []
    for a in range(x):
        l1.append([])
        for b in range(y):
            d = a * b
            l1[a].append(a*b)
    print(l1)
    return
two_dimens_arr(4, 4)