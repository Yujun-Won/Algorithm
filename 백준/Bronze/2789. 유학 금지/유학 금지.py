prohibited = list("CAMBRIDGE")

inputStr = input()
result = [string for string in inputStr if string not in prohibited]

print(''.join(result))
