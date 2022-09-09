from itertools import combinations
arr = input()
stack = []
tmp = []
answer = set()

for idx, w in enumerate(arr):
    if w == '(':
        stack.append(idx)
    elif w == ')':
        tmp.append((stack.pop(), idx))

for i in range(1, len(tmp) + 1):
    comb = combinations(tmp, i)
    for j in comb:
        target = list(arr)
        for k in j:
            start, end = k
            target[start] = ''
            target[end] = ''
        answer.add(''.join(target))

for ans in sorted(list(answer)):
    print(ans)

