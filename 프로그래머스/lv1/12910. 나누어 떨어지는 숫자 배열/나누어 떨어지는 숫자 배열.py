def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    
    if answer == []:
        answer = [-1]
    else:
        answer.sort()
    return answer