# {소문자: 숫자}의 구조를 가진 딕셔너리 생성
alpha_num = {chr(i+96): i for i in range(1, 27)}

L = int(input())        # 문자열의 길이
st = input()            # 문자열

temp = []
for i in st:            # 문자열을 숫자 리스트로 변환
  temp.append(alpha_num[i])

result = 0
for i in range(L):      # 해시 값 변환
  result += temp[i] * (31**i)

print(result)