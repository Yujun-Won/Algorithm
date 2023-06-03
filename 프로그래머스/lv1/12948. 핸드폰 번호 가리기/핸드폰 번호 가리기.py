def solution(phone_number):
    stars = len(phone_number) - 4
    
    answer = '*' * stars + phone_number[stars:]
    return answer