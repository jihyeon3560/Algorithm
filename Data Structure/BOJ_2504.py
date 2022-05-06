S = list(input())
stack = []

ans = 0
tmp = 1
for i in range(len(S)):

    if S[i] == '(':
        stack.append(S[i])
        tmp *= 2
    elif S[i] == '[':
        stack.append(S[i])
        tmp *= 3

    elif S[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break

        if S[i-1] == '(':
            ans += tmp
        tmp //= 2
        stack.pop()

    elif S[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break

        if S[i-1] == '[':
            ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)