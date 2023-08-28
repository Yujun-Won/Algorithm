studentList = []

for _ in range(int(input())):
    name, korean, english, math = input().split()
    studentList.append([name, int(korean), int(english), int(math)])

studentList.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in studentList:
    print(student[0])
