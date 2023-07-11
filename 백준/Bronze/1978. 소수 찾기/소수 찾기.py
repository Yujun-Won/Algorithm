def isPrime(num):
    if num == 1:
      return False
    for i in range(2, num):
    	if num % i == 0:
        	return False
    return True

N = int(input())
nums = list(map(int, input().split()))

result = []
for j in nums:
  if isPrime(j) is True:
    result.append(j)
print(len(result))