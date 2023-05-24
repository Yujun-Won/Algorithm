def solution(s):
    str_list = list(s.split(' '))
    
    result = []
    for string in str_list:
        answer = ''
        for idx in range(len(string)):
            if idx % 2 == 0:
                answer += string[idx].upper()
            else:
                answer += string[idx].lower()
        result.append(answer)
    
    answer = ' '.join(result)
    return answer