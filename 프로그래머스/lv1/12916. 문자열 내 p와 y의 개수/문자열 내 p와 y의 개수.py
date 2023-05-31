def solution(s):
    cntP, cntY = 0, 0
    for i in s:
        if i in ['p', 'P']:
            cntP += 1
        elif i in ['y', 'Y']:
            cntY += 1
    
    answer = False
    if cntP == cntY:
        answer = True
    
    return answer