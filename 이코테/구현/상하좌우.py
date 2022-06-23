n = int(input())
arr = list(input().split())

di = [0,0,-1,1]
dj = [-1,1,0,0]
d = {'L': 0,
     'R': 1,
     'U': 2,
     'D': 3}
ans = [1,1]
for k in arr:
    ni = ans[0] + di[d[k]]
    nj = ans[1] + dj[d[k]]
    if 1 <= ni <=n and 1 <= nj <= n:
        ans = [ni, nj]

print(*ans)

# 답안코드
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types = ['L','R','U','D']
#
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x, y)