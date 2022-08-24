N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

#정렬
arr.sort(reverse=True)
first = arr[0]
second = arr[1]
ans = 0

while True:
    for i in range(K):
        if M == 0:
            break
        ans += first
        M -= 1
    if M == 0:
        break
    ans += second
    M -= 1

print(ans)

# 다른 풀이
# count = int(M/(K+1)) * K
# count += M % (K+1)
#
# ans = 0
# ans += count*first
# ans += (M-count)*second
#
# print(ans)