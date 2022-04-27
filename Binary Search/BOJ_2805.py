N, M = map(int, input().split())
tree = list(map(int, input().split()))

l, r = 1, max(tree)

while l <= r:
    mid = (l+r)//2
    height = 0
    for i in tree:
        if i >= mid:
            height += i - mid
    if height >= M:
        l = mid + 1
    else:
        r = mid - 1

print(r)
