from itertools import combinations

N, M = map(int, input().split())

result = list(combinations(list(range(1, N+1)), M))

for res in result:
    answer = ''.join(str(list(res))).replace('[', '').replace(']', '').replace(',', '')
    print(answer.strip())
