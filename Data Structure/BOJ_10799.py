arr = input()
stack = []
ans = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(i)
        cnt += 1
        ans += 1
    else:
        if arr[i-1] == '(':
            stack.pop()
            cnt -= 1
            ans -= 1
            ans += cnt
        else:
            stack.pop()
            cnt -= 1

print(ans)
