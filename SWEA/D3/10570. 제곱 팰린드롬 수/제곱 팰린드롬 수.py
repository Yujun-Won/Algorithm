def is_palindrome(number):
    # 입력된 숫자가 팰린드롬 수인지 찾는 함수
    return str(number) == str(number)[::-1]

def is_square_palindrome(number):
    # 입력된 숫자의 제곱근이 팰린드롬 수인지 찾는 함수
    root_num = int(number ** 0.5)
    return root_num * root_num == number and is_palindrome(root_num)

testcase = int(input())

for i in range(testcase):
    A, B = map(int, input().split())

    cnt = 0
    for number in range(A, B+1):
        if is_square_palindrome(number) and is_palindrome(number):
            cnt += 1

    print(f"#{i+1} {cnt}")
