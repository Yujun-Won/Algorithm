num, idx = map(int, input().split())
divisor = [i for i in range(1, num+1) if num%i==0]

if idx > len(divisor):
    print(0)
else:
    print(divisor[idx-1])