def prog_1(x):
    dict_ = dict()
    for a in range(1, x+1):
        dict_[a] = a*a
    print(dict_.__str__())
print("Exercise_3: input like 8, 7 or 9")
prog_1(int(input()))
