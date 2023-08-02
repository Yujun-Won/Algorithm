def solution(s, n):
    upperAlpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowerAlpha = list(('ABCDEFGHIJKLMNOPQRSTUVWXYZ').lower())
    
    answer = []
    
    for digit in s:
        if digit in upperAlpha:
            new_idx = upperAlpha.index(digit) + n
            if new_idx > 25:
                new_idx -= 26
            answer.append(upperAlpha[new_idx])
        elif digit in lowerAlpha:
            new_idx = lowerAlpha.index(digit) + n
            if new_idx > 25:
                new_idx -= 26
            answer.append(lowerAlpha[new_idx])
        elif digit == ' ':
            answer.append(' ')
    
    result = ''
    for i in answer:
        result += i
    return result