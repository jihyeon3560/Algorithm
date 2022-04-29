import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = arr[i] + arr[j] + arr[k]

            if total <= M:
                if ans < total:
                    ans = total
print(ans)
