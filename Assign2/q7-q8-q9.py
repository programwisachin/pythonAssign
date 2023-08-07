# q7

def prog_7():
    x = input()
    list_ = []

    for a in x.split(","):
        list_.append(a)
    list_.sort()
    str_ = ",".join(list_)
    print(list_)
    return

prog_7()

# q8
def prog_8():
    x = input()
    set_ = set((x.split()))
    list_ = [x for x in set_]
    list_.sort()
    print(" ".join(x for x in list_))
prog_8()


# q9
def prog_9():
    x = input().split(",")
    print(x)
    list_ = []
    for a in x:
        list_.append(int(a))
    list_2 = [a for a in list_ if a % 5 == 0]
    print(list_2)
prog_9()