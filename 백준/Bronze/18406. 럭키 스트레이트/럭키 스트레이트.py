n = input()

left = list(map(int, n[0:len(n)//2]))
right = list(map(int, list(n[len(n)//2:len(n)])))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")

