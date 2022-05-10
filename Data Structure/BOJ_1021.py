from collections import deque

N, M = map(int, input().split())
pos = list(map(int, input().split()))
dq = deque([i+1 for i in range(N)])

cnt = 0
for i in pos:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)