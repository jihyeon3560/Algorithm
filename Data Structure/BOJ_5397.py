T = int(input())

for t in range(T):
    pw = list(input())
    left = []
    right = []

    for i in pw:

        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    left.extend(reversed(right))

    print(''.join(left))
