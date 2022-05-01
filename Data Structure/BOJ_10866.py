import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    tmp = list(sys.stdin.readline().split())

    if tmp[0] == 'push_front':
        queue.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        queue.append(tmp[1])
    elif tmp[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif tmp[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(queue))
    elif tmp[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif tmp[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
