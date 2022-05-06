import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])
for _ in range(N):
    s = list(sys.stdin.readline().split())

    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif s[0] == 'size':
        print(len(q))

    elif s[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif s[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
