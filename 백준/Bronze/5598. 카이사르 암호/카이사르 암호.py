alphabets = [chr(i + 65) for i in range(26)]

inputStr = input()
result = ''
for string in inputStr:
    if string not in ['X', 'Y', 'Z']:
        result += alphabets[alphabets.index(string) - 3]
    elif string == 'X':
        result += 'U'
    elif string == 'Y':
        result += 'V'
    elif string == 'Z':
        result += 'W'

print(result)
