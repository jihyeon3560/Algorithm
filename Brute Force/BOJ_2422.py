import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[1]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = arr[b][a] = 0

result = []
for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            if arr[i][j] and arr[i][k] and arr[j][k]:
                result.append([i,j,k])


print(len(result))
