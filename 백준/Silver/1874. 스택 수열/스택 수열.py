n = int(input())

cnt = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())

    while cnt <= data:          # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if stack[-1] == data:       # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else:                       # 불가능한 경우
        print('NO')
        exit(0)

print('\n'.join(result))        # 가능한 경우