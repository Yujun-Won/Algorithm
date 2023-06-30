D, H, W = map(int, input().split())
k = D / ((H**2 + W**2) ** 0.5)

print(int(H*k), int(W*k))