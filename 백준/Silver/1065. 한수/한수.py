import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

if N <= 99:
    cnt = N
else:
    cnt += 99
    for num in range(100, N+1):
        number = list(str(num))
        temp = []
        for i in range(len(number)-1):
            diff = int(number[i+1]) - int(number[i])
            temp.append(diff)

        if all(x == temp[0] for x in temp):
            cnt += 1

print(cnt)
