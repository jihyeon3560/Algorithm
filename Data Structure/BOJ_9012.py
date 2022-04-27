import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = list(sys.stdin.readline().strip())

    stack = []
    isVPS = 1

    for i in range(len(s)):
        if i == 0 and s[i] == ')':
            isVPS = 0
            break
        if s[i] == '(':
            stack.append(s[i])

        else:
            if not stack:
                isVPS = 0
                break
            stack.pop()
    if stack:
        isVPS = 0

    if isVPS:
        print('YES')
    else:
        print('NO')