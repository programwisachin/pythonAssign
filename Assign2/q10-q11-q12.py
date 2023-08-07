# q10
import math
def prog_10():
    n_ = []
    str_num_ = ""
    for a in range(1000, 3001):
        str_num_ = str(a)
        indicator_ = 0
        for i in str_num_:
            if int(i)%2 == 0:
                indicator_ += 1
        if indicator_ == 4:
            n_.append(a)
    print(n_)
    return
prog_10()

#q11
str_ = str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])
print("Python version: " + str_)

#q12


def prog_12():
    radius  = int(input())
    print("Area for radius: " + str(radius) + " is " + str(math.pi * math.pow(radius, 2)))
prog_12()