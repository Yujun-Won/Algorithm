def solution(s):
    result = ''
    is_new_word = True
    for char in s:
        if char == ' ':
            result += char
            is_new_word = True
        elif is_new_word:
            result += char.upper()
            is_new_word = False
        else:
            result += char.lower()
    return result
