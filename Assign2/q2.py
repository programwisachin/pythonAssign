
def fact_1(x):
    b = 1
    for a in range(1, x+1):
        b *= a
    return b
print("Exercise_2: Solution_1(input like 8 or 9)")
x = int(input())
print(fact_1(x))