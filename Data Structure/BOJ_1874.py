import sys

N = int(sys.stdin.readline())

stack = []
result = []
idx = 0
is_stack = True
for _ in range(N):
    x = int(sys.stdin.readline())

    while idx < x:
        idx += 1
        stack.append(idx)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        is_stack = False

if is_stack:
    for i in result:
        print(i)
else:
    print('NO')
