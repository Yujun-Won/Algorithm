a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print("Equilateral")
elif a+b+c == 180 and (a==b!=c or b==c!=a or c==a!=b):
    print("Isosceles")
elif a+b+c == 180 and a!=b!=c:
    print("Scalene")
else:
    print("Error")