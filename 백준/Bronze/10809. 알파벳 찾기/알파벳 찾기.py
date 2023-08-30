alphabets = [chr(i+97) for i in range(26)]
result = [-1] * len(alphabets)

inputStr = list(input())

for idx, string in enumerate(inputStr):
    if result[alphabets.index(string)] == -1:
        result[alphabets.index(string)] = idx
    else:
        pass

for digit in result:
    print(digit, end=" ")
print()