def osszeadas(tesztesetek):
    for i in range(tesztesetek):
        while True:
            a = str(input("elso szam:"))
            if 1<=int(a)<=10**9:
                break
        while True:
            b = str(input("masodik szam:"))
            if 1<=int(b)<=10**9:
                break
        megoldas = ""
        hosszabb=a
        rovidebb=b
        if len(hosszabb) < len(rovidebb):
            hosszabb, rovidebb = rovidebb, hosszabb
        for i in range(len(hosszabb) - 1, -1, -1):
            if i > (len(rovidebb) - 1):
                megoldas += hosszabb[len(hosszabb) - 1 - i]
            else:
                szam = int(hosszabb[len(hosszabb) - 1 - i]) + int(rovidebb[len(rovidebb) - 1 - i])
                if szam >= 10:
                    szam -= 10
                megoldas += str(szam)
        print(megoldas)

while True:
    tesztesetek=int(input("tesztesetek szama: "))
    if 1<=tesztesetek<=100:
        break
osszeadas(tesztesetek)