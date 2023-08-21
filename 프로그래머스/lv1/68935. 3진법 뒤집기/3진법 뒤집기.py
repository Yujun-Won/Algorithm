def solution(n):
    def radixTransform(decimal_num, base):
        if decimal_num == 0:
            return '0'
        
        result = ''
        while decimal_num > 0:
            decimal_num, remainder = divmod(decimal_num, base)
            result = str(remainder) + result
        
        return result
    
    # 1. 3진수화
    ternary_num = radixTransform(n, 3)
    
    # 2. 10진수화
    result = 0
    for i, digit in enumerate(ternary_num):
        result += int(digit) * (3 ** int(i))
    
    return result
