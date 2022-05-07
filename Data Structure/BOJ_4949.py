while True:
    s = list(input())
    stack = []
    ans = 'yes'
    # 종료 조건
    if s[0] == '.' and len(s) == 1:
        break

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == '[':
            stack.append(s[i])

        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                ans = 'no'
                break
            elif stack[-1] == '(':
                stack.pop()

        elif s[i] == ']':
            if not stack or stack[-1] == '(':
                ans = 'no'
                break
            elif stack[-1] == '[':
                stack.pop()
    if stack:
        print('no')
    else:
        print(ans)