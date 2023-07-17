people = []

for i in range(4):
    a, b = map(int, input().split())
    if i == 0:
        people.append(a)
        people.append(b)
    else:
        nowIn = people[-1]
        people.append(nowIn - a)
        nowIn = people[-1]
        people.append(nowIn + b)

print(max(people))