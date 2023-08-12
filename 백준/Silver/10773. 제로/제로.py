stk = []

for _ in range(int(input())):
    num = int(input())
    if num != 0:
        stk.append(num)
    else:
        stk.pop()
print(sum(stk))