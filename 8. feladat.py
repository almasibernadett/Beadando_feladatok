def hazifeladat(tesztesetek):
    for i in range(tesztesetek):
        while True:
            n = int(input("Feladatok szama: "))
            if 1<=n<=10**8:
                break
        while True:
            b = int(input("Szunetek hossza: "))
            if 1<=b<=10**8:
                break
        while True:
            m = int(input("Feladatok megoldasanak ideje:"))
            if 1<=m<=10**8:
                break
        ido = 0
        while n != 0:
            if n != 1:
                if n % 2 == 0:
                    ido += (n / 2 * m) + b
                    n = n - (n / 2)
                    m *= 2
                else:
                    n += 1
                    ido += (n / 2 * m) + b
                    n = n - (n / 2) - 1
                    m *= 2
            else:
                ido += m
                n = 0
        print(round(ido))
while True:
    tesztesetek=int(input("Tesztesetek szama: "))
    if 1<=tesztesetek<=100:
        break
hazifeladat(tesztesetek)


