for _ in range(int(input())):
    inputStr = list(input().split())
    result = [string[::-1] for string in inputStr]

    print(" ".join(result))
