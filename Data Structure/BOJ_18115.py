from collections import deque

N = int(input())
tech = list(map(int, input().split()))
arr = list(i+1 for i in range(N-1, -1, -1))
tech.reverse()
result = deque([])

for i in range(N):
    a = arr.pop()

    if tech[i] == 1:
        result.append(a)

    elif tech[i] == 2:
        b = result.pop()
        result.append(a)
        result.append(b)

    elif tech[i] == 3:
        result.appendleft(a)

result.reverse()
print(*result)
