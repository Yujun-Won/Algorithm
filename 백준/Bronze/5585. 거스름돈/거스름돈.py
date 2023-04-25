exchange = 1000 - int(input())

coinList = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coinList:
    cnt += exchange // coin
    exchange %= coin
print(cnt)