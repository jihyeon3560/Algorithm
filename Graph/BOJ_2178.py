from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0<= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            queue.append((nx, ny))


print(arr[n-1][m-1])