from collections import deque
import sys

q = deque()

for _ in range(int(sys.stdin.readline().rstrip())):
    cmd = sys.stdin.readline().rstrip()
    if "push_back" in cmd:
        temp = list(cmd.split())
        q.append(int(temp[1]))
    elif "push_front" in cmd:
        temp = list(cmd.split())
        q.appendleft(int(temp[1]))
    elif "pop_front" in cmd:
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif "pop_back" in cmd:
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif "front" in cmd:
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif "back" in cmd:
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
    elif "size" in cmd:
        print(len(q))
    elif "empty" in cmd:
        if len(q) == 0:
            print(1)
        else:
            print(0)