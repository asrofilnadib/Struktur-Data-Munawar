def buble():
    numlist = [5, 34, 32, 25, 75, 42, 22, 2]

    print("Data sebelum diurutkan")
    print(numlist)

    for i in numlist:
        for j in numlist(0, -i-1):
            if j < i:
                temp = numlist[j]
                numlist[j] = numlist[j - 1]
                numlist[j-1] = temp


buble()