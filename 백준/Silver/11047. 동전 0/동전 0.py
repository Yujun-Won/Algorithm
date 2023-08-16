N, K = map(int, input().split())
coinList = [int(input()) for _ in range(N)]
coinList.reverse()

cnt = 0
for coin in coinList:
  cnt += K // coin            # K를 coin으로 나눈 몫을 cnt에 저장  
  K %= coin                   # K를 coin으로 나눈 나머지로 K를 업데이트
  # print(coin, K, cnt)
  
print(cnt)