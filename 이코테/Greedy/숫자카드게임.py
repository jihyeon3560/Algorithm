n, m = map(int, input().split())
ans = 0
for i in range(n):
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] >= ans:
        ans = lst[0]

print(ans)

