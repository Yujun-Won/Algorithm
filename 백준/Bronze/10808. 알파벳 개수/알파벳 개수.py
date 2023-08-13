S = input()

count = [0] * 26
for digit in S:
    count[ord(digit)-97] += 1

for i in count:
    print(i, end=" ")
print()