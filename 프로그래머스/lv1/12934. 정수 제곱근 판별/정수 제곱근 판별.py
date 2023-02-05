import math as m

def solution(n):
    answer = 0
    if m.ceil(m.sqrt(n)) != m.floor(m.sqrt(n)):
        answer = -1
    else:
        answer = (m.sqrt(n)+1) ** 2
    return answer