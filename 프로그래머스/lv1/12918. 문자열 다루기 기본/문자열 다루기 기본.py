def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
        if s.isdigit():
            answer = True
        else:
            answer = False
    
    return answer