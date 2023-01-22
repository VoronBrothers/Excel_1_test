a = 10
b = 15


def nod(arg=15, barg=20):
    # help
    if arg < barg:
        arg, barg = barg, arg
    print(f"{arg}, {barg} - значения a and b")

    while barg != 0:
        print(f"{barg} - значение Б")
        arg, barg = barg, arg % barg

    return arg


print(nod(25, 45))
