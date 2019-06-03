# 4 kjyu
def snail(x):

    res = []
    top_bottom(x, res)
    print(res)
    print([1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
          )

    return res


def top_bottom(x, res):
    i = 0
    is_running = True
    while is_running:
        # get the first row of the array forward

        if i == 0:
            for ele in x[0]:
                res.append(ele)
        # in between take the last the index
        if i > 0 and i < len(x) - 1:
            res.append(x[i][len(x[i]) - 1])
            del x[i][len(x[i]) - 1]
        # get the last row backward of the array
        if i == len(x) - 1 and len(x) != 1:
            for ele in range(len(x[i])):
                res.append(x[i][len(x[i]) - 1 - ele])

            for ele in range(len(x) - 2):
                res.append(x[len(x) - 2 - ele][0])
                del x[len(x) - 2 - ele][0]
                if len(x) - 2 - ele == 0:
                    break
        if i == len(x) and len(x) != 1:
            del x[0]
            del x[len(x) - 1]
            break

        if len(x) == 1:
            del x[0]
            is_running = False
            break
        i += 1
    if len(x) != 0:
        print(res)
        top_bottom(x, res)


# snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
# snail([[1, 2, 3, 4, 5],
#        [6, 7, 8, 9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

# snail([[499, 26, 257, 454, 407, 481, 421, 171, 222, 511],
#        [520, 122, 385, 931, 636, 988, 313, 594, 889, 450],
#        [323, 12, 979, 848, 295, 192, 322, 172, 625, 500],
#        [879, 157, 729, 761, 948, 206, 905, 155, 852, 912],
#        [674, 861, 602, 425, 608, 879, 328, 41, 215, 285],
#        [507, 985, 362, 824, 985, 987, 780, 968, 76, 879],
#        [451, 868, 398, 764, 394, 323, 410, 866, 234, 503],
#        [496, 449, 1000, 337, 778, 269, 240, 249, 601, 156],
#        [449, 776, 513, 92, 95, 140, 245, 859, 249, 811],
#        [401, 979, 192, 877, 500, 415, 537, 125, 376, 998]]
#       )

# [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
