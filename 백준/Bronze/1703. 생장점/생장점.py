while True:
    tree = list(map(int, input().split()))
    if tree[0] == 0:
        break
    else:
        branch = 1
        for i in range(1, len(tree)):
            if i % 2 != 0:      # 홀수번째 입력
                branch *= tree[i]
            elif i % 2 == 0:    # 짝수번째 입력
                branch -= tree[i]
    print(branch)
