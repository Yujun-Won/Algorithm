for _ in range(int(input())):
    inputs = list(input().split())
    
    temp = eval(f"{inputs[0]}{inputs[1]}{inputs[2]}")
    if temp == int(inputs[4]):
        print("correct")
    else:
        print("wrong answer")