def sum_digit(n):
    n = str(n)
    while len(n) > 1:
        n = str(sum(int(ele) for ele in n))
    print(n)
    return int(n)


# sum_digit(942)
