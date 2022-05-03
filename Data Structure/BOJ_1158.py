from collections import deque

N, K = map(int, input().split())
q = deque()
for i in range(N):
    q.append(i+1)

idx = 0
result = []
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    result.append(str(q.popleft()))

print('<' + ', '.join(result) + '>')
