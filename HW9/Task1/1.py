def diclist(slist):
    list = [1, 2, 3, 4]
    for elem in list:
        slist.extend([elem] * 2)
    print(slist)

    