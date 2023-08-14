import sys

number = sys.stdin.readline().rstrip()

# 8진수 -> 2진수 변환 테이블
oct_to_bin = {
    '0': '000',
    '1': '001',
    '2': '010',
    '3': '011',
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111'
}

# 8진수의 각 자릿수를 2진수로 변환
binaryNumber = ''.join(oct_to_bin[digit] for digit in number)

# 앞쪽의 불필요한 0 제거
binaryNumber = binaryNumber.lstrip('0')

# 결과가 빈 문자열이면 0 출력
if not binaryNumber:
    print(0)
else:
    print(binaryNumber)
