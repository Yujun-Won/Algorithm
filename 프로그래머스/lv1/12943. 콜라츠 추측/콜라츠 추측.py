def solution(num):
    cnt = 0
    while True:
        if num == 1:
            break
        if cnt == 500:
            cnt = -1
            break
            
        if num % 2 == 0:            # 입력된 수가 짝수
            num /= 2
            cnt += 1
        else:                       # 입력된 수가 홀수
            num = 3 * num + 1
            cnt += 1
    return cnt