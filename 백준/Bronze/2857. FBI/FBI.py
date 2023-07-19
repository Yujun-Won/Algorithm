spies = []
for _ in range(5):
    spies.append(input())

result = []
for spy in spies:
    if "FBI" in spy:
        result.append(spies.index(spy)+1)

if len(result) == 0:
    print("HE GOT AWAY!")
else:
    for i in result:
        print(i, end=" ")
    print()