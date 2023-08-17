while True:
    cipher = input()
    if cipher == "END":
        break
    else:
        print(cipher[::-1])