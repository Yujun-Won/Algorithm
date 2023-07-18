for _ in range(3):
    lst = list(map(int, input().split()))
    
    cnt = lst.count(1)
    if cnt == 3:
        print("A")  # 도
    elif cnt == 2:
        print("B")  # 개
    elif cnt == 1:
        print("C")  # 걸
    elif cnt == 0:
        print("D")  # 윷
    else:
        print("E")  # 모