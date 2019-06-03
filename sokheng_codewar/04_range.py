import time
# 4kjyu
start_time = time.time()


def range(args):
    res = []
    final_res = []
    store_res = []
    i = 0
    for ele in args:
        print("this is every ele", ele)
        is_running = True
        if ele in store_res:
            continue
        else:
            while is_running:

                if ele + i in args:
                    res.append(str(ele + i))
                    store_res.append(ele + i)
                else:
                    print('This store res', store_res)
                    print("res", res)
                    if len(res) >= 3:
                        store = res[0] + '-' + res[len(res) - 1]
                        final_res.append(store)
                    else:
                        del store_res[len(store_res) - 1]
                        final_res.append(str(ele))
                    i = 0
                    res = []
                    print(final_res)
                    break
                i += 1

    print(final_res)


range([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20])
print("--- %s seconds ---" % (time.time() - start_time))
