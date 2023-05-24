T = int(input())

for i in range(1, T+1):
    word = input()

    if word == word[::-1]:
        answer = 1 
    else:
        answer = 0
        
    print(f"#{i} {answer}")