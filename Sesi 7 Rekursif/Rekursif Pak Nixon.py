def rekursif(l):
    n = l
    hfak = 1
    i = 1
    while i <= n:
        hfak = hfak * i
        i += 1
    print(hfak)


x = input("Masukan angka: ")
y = int(x)
rekursif(y)
