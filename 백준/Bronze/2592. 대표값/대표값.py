from collections import Counter

numbers = [int(input()) for _ in range(10)]

mode = Counter(numbers).most_common()

print(sum(numbers) // 10)
print(mode[0][0])
