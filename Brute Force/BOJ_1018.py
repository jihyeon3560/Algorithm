n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
cnt = []
# 8x8로 자르기
for i in range(n-8+1):
    for j in range(m-8+1):
        #시작 흰
        index1 = 0
        #시작 검
        index2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        index1 += 1
                    if board[a][b] != 'B':
                        index2 += 1
                else:
                    if board[a][b] != 'B':
                        index1 += 1
                    if board[a][b] != 'W':
                        index2 += 1
        cnt.append(min(index1,index2))
print(min(cnt))
