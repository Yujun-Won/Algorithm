L, P = map(int, input().split())
participants = list(map(int, input().split()))

result = [part-L*P for part in participants]

for i in result:
    print(i, end=" ")
print()