alphabets = [chr(i+65) for i in range(26)]

n = int(input())
grid = [[0 for i in range(n)] for i in range(n)]

idx = 0

for j in range(n):
    for i in range(n):
        if j % 2 == 0:          # i가 짝수일 때 (정방향)
            if idx < 26:
                grid[i][j] = alphabets[idx]
            else:
                idx -= 26
                grid[i][j] = alphabets[idx]
        else:                   # i가 홀수일 때 (역방향)
            if idx < 26:
                grid[n-i-1][j] = alphabets[idx]
            else:
                idx -= 26
                grid[n-i-1][j] = alphabets[idx]
        idx += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
