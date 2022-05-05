n = int(input())
idx = 0
result = []

arr = list(map(int, input().split()))
index = [x for x in range(1, n + 1)]

temp = arr.pop(idx)
result.append(index.pop(idx))

while arr:
    if temp < 0:
        idx = (idx + temp) % len(arr)
    else:
        idx = (idx + (temp - 1)) % len(arr)
    temp = arr.pop(idx)
    result.append(index.pop(idx))

for r in result:
    print(r, end=' ')