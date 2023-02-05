def solution(left, right):
    count = 0
    temp = []
    for num in range(left, right+1):
        divCnt = 0
        for i in range(1, num+1):
            if num % i == 0: 
                divCnt += 1
        temp.append(divCnt)
    
    idx, answer = 0, 0
    for i in range(left, right+1):
        if temp[idx] % 2 == 0:
            answer += i
        else:
            answer -= i
        idx += 1
    return answer