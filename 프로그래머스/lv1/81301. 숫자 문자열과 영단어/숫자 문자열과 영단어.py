def solution(s):
    numDict = {'zero': '0', 'one': '1', 'two': '2',
               'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
              }
    
    result = ''
    temp = ''
    for digit in s:
        if digit in '0123456789':
            result += digit
        else:
            temp += digit
            if temp in numDict.keys():
                result += numDict[temp]
                temp = ''
    return int(result)
            