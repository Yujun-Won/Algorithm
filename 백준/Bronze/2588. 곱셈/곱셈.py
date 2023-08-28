N = int(input())
M = input()

for i in M[::-1]:
    print(N * int(i))

print(N * int(M))