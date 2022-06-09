T = int(input())

# 함수 사용
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))

# 함수 사용 X
# for t in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     mmin = 987654321
#     mmax = -987654321
#     for i in range(N):
#         if arr[i] > mmax:
#             mmax = arr[i]
#         if arr[i] < mmin:
#             mmin = arr[i]
#     print(mmin, mmax)

