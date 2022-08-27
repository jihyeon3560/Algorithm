# import sys
# sys.setrecursionlimit(10**6)

from collections import deque

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,1,-1,-1]

# def dfs(x,y):
#     arr[x][y] = 0
#     for k in range(8):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
#             dfs(nx, ny)


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    # 지도
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)


