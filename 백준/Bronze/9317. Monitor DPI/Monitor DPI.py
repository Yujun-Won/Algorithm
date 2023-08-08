while True:
    d, resH, resV = map(float, input().split())
    if d == resH == resV == 0:
        break
    else:
        w = 16 * d / (337 ** 0.5)
        h = w * 9 / 16
        print("Horizontal DPI: {:.2f}".format(resH/w))
        print("Vertical DPI: {:.2f}".format(resV/h))