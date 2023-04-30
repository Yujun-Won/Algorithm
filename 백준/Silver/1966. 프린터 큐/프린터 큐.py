import sys

testcases = int(sys.stdin.readline())

for _ in range(testcases):
    n, m = list(map(int, sys.stdin.readline().split()))
    queue = list(map(int, sys.stdin.readline().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    cnt = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))