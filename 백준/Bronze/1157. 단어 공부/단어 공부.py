word = input().upper()
only_word = list(set(word))       # 중복값 제거

cnt = []
for i in only_word:
    cnt.append(word.count(i))     # cnt 리스트 생성

if cnt.count(max(cnt)) > 1 :      # cnt 숫자 최대값이 여러 개이면
    print('?')
else :
    idx = cnt.index(max(cnt))     # cnt 숫자 최대값 인덱스
    print(only_word[idx])