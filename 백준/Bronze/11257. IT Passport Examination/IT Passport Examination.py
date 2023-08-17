passNum = []
strategys = []
itManages = []
technologies = []

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    passNum.append(a)
    strategys.append(b)
    itManages.append(c)
    technologies.append(d)

    if b+c+d >= 55:
        if b >= 35*0.3 and c >= 25*0.3 and d >= 40*0.3:
            result = "PASS"
        else:
            result = "FAIL"
    else:
        result = "FAIL"
    print(f"{a} {b+c+d} {result}")
