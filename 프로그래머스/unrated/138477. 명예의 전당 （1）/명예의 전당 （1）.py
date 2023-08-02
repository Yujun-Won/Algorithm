def solution(k, score):
    answer = []
    result = []
    
    for i in score:
        if len(answer) < 3:
            answer.append(i)
            answer = sorted(answer, reverse=True)
            result.append(answer[-1])        
        else:
            temp = answer.pop()
            if i < temp:
                answer.append(temp)
                pass
            else:
                answer.append(i)
                answer = sorted(answer, reverse=True)
                result.append(answer[-1])
            
    return result