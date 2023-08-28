radixDict = {chr(i): i - ord('A') + 10 for i in range(ord('A'), ord('Z') + 1)}

N, B = input().split()
result = 0

for i, num in enumerate(N[::-1]):
    if '0' <= num <= '9':
        result += int(num) * (int(B) ** i)
    else:
        result += (ord(num) - ord('A') + 10) * (int(B) ** i)

print(result)
