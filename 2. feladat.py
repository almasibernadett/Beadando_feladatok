while True:
    n=int(input("tesztesetek szama: "))
    if 1<=n<=1000:
        break

for i in range(n):
    res=""
    while True:
        v=int(input("Penzosszeg erteke: "))
        if 1<=v<=100000:
            break
    szaz=v//100
    v=v%100
    otven=v//50
    v=v%50
    tiz=v//10
    v=v%10
    ot=v//5
    v=v%5
    ketto=v//2
    v=v%2
    egy=v
#    print("{}db 100Ft; {}db 50Ft; {}db 10Ft; {}db 5Ft; {}db 2Ft; {}db 1Ft".format(szaz,otven,tiz,ot,ketto,egy))
    if szaz!=0:
        res+=("{}db 100Ft".format(szaz))
    if otven!=0:
        res+=("; {}db 50Ft".format(otven))
    if tiz!=0:
        res+=("; {}db 10 Ft".format(tiz))
    if ot!=0:
        res+=("; {}db 5Ft".format(ot))
    if ketto!=0:
        res+=("; {}db 2Ft".format(ketto))
    if egy!=0:
        res+=("; {}db 1Ft".format(egy))
    print(res)