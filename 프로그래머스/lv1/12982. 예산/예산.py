def solution(d, budget):
    d = sorted(d)                   # d를 정렬

    tot, cnt = 0, 0
    for i in range(len(d)):
        if tot + d[i] <= budget:    # 누적합 + 새로 들어올 수의 합 <= 예산
            tot += d[i]
            cnt += 1
        else:
            break
    return cnt