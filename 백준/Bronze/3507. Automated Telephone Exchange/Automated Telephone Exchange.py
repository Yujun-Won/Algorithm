ate = int(input())
cnt = 0

if ate <= 198:
    for i in range(100):
        for j in range(100):
            if i + j == ate:
                cnt += 1
print(cnt)