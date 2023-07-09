scene = 0
while True:
    o, w = map(int, input().split())
    
    if o == 0 and w == 0:
        break

    die = False
    while True:
        cmd, n = input().split()
        if cmd == "#" and n == "0":
            break

        if not die:
            if cmd == 'F':
                w += int(n)
            elif cmd == 'E':
                w -= int(n)
            
        if w <= 0:  # 사망
            die = True

    scene += 1
    if w <= 0:
        print(f"{scene} RIP")
    elif 0.5*o < w < 2*o:
        print(f"{scene} :-)")
    else:
        print(f"{scene} :-(")