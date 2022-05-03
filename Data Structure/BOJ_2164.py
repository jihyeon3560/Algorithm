from collections import deque

N = int(input())
q = deque()
for i in range(N):
    q.append(i+1)

while len(q) > 1:
    a = q.popleft()
    b = q.popleft()
    q.append(b)
print(*q)