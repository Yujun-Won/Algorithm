notUse = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

words = list(input().split())
temp = []

for word in words:
    if word is words[0] and word in notUse: # 쓸모없는 단어이지만 말의 맨 앞에 올 경우
        temp.append(word)
    elif word not in notUse:                # 쓸모없는 단어를 제외한 결과
        temp.append(word)

answer = ''.join([i[0].upper() for i in temp])
print(answer)