n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def dfs(x, y):
    arr[x][y] = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            dfs(nx, ny)


for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            dfs(x, y)
            cnt += 1

print(cnt)



