student = list(range(1, 31))

done = []
for _ in range(28):
  n = int(input())
  done.append(n)

for i in done:
  if i in student:
    student.remove(i)

print(student[0])
print(student[1])