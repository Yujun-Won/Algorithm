T = int(input())

for _ in range(T):
    tot, gpa = 0, 0
    for i in range(int(input())):
        a, b = map(float, input().split())
        tot += a
        gpa += (a * b)
    print(int(tot), round(gpa/tot, 1))