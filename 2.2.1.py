def Sort_Tuple(tup):

    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][-1] > tup[j + 1][-1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


tup = [(1, 3), (3, 2), (2, 1)]
print("The sorted is:")
print(Sort_Tuple(tup))
