import sys

students = []
for _ in range(int(sys.stdin.readline().rstrip())):
    weight, height = map(int, sys.stdin.readline().rstrip().split())
    students.append((weight, height))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
print()
