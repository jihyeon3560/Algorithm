import sys

N = int(sys.stdin.readline())
equal = sys.stdin.readline().strip()
alph = []
op = ['+', '-', '*', '/']
for _ in range(N):
    alph.append(int(sys.stdin.readline()))

stack = []
for i in equal:
    if i in op:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i == '/':
            stack.append(a/b)
    else:
        stack.append(alph[ord(i)-ord('A')])
print(f'{stack[0]:.2f}')