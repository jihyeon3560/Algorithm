import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
result = ''
total = 0
# 비교
for i in range(M):
    cnt_A = cnt_T = cnt_G = cnt_C = 0
    # 갯수세기
    for j in range(N):
        if arr[j][i] == 'A':
            cnt_A += 1
        elif arr[j][i] == 'T':
            cnt_T += 1
        elif arr[j][i] == 'G':
            cnt_G += 1
        elif arr[j][i] == 'C':
            cnt_C += 1

   # 가장 많은 것을 채택하면 최소가 됨
    part_max =  max(cnt_A, cnt_T, cnt_G, cnt_C)
    if part_max == cnt_A:
       result += 'A'
    elif part_max == cnt_C:
       result += 'C'
    elif part_max == cnt_G:
       result += 'G'
    elif part_max == cnt_T:
        result += 'T'

    total += N-part_max

print(result)
print(total)