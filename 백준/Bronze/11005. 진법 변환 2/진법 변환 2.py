radixDict = {i - ord('A') + 10: chr(i) for i in range(ord('A'), ord('Z') + 1)}

N, B = map(int, input().split())
result = []

while N > 0:
    res = N % B
    N //= B

    if 0 <= res <= 9:
        result.append(str(res))
    else:
        result.append(radixDict[res])

print(''.join(result[::-1]))
