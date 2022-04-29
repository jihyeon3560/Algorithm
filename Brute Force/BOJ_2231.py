N = int(input())

M = 1
flag = 1
while M < N:
    total = 0
    k = M
    while k > 0:
        total += (k % 10)
        k = k // 10
    if total + M == N:
        print(M)
        flag = 0
        break
    else:
        M += 1


if flag:
    print(0)