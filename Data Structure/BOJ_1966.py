T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = [arr[i], i]

    ans = 0

    while arr:
        max_V = max(t[0] for t in arr)
        if max_V == arr[0][0]:
            n = arr.pop(0)
            ans += 1
            if n[1] == m:
                print(ans)
                break
        else:
            arr.append(arr.pop(0))