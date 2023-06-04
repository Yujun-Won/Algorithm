def solution(lottos, win_nums):
    # 변할 수 있는 수
    zeros = lottos.count(0)
    
    # 이미 고정된 수
    cnt = 0
    for num in win_nums:
        if num in lottos:
            cnt += 1
    
    temp = [cnt+zeros, cnt]
    result = []
    for i in temp:
        if i == 6:
            result.append(1)
        elif i == 5:
            result.append(2)
        elif i == 4:
            result.append(3)
        elif i == 3:
            result.append(4)
        elif i == 2:
            result.append(5)
        else:
            result.append(6)
    
    return result
