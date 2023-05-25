def power(num, n):
    if n == 1:
        return num
    else:
        return num * power(num, n-1)
    
for _ in range(10):
    testcase = int(input())
    N, M = map(int, input().split())
    
    print(f"#{testcase} {power(N, M)}")