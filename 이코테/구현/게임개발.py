n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[x][y] = 1

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    #방문, 바다 확인
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)




