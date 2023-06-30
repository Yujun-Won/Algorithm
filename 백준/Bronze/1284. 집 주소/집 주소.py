while True:
    space = 0
    number = input()
    if number == '0':
        break
    else:
        space += 2                  # 양 끝의 여백
        space += (len(number)-1)    # 숫자 사이 여백
        for i in number:            # 숫자 너비
            if i == '1':
                space += 2
            elif i == '0':
                space += 4
            else:
                space += 3
        print(space)