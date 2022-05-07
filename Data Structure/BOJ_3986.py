N = int(input())
ans = 0
for _ in range(N):
    words = input()
    stack = []

    for i in range(len(words)):

        if not stack:
            stack.append(words[i])
        else:
            if stack[-1] == words[i]:
                stack.pop()
            else:
                stack.append(words[i])

    if not stack:
        ans += 1

print(ans)