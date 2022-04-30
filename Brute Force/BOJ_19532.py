a, b, c, d, e, f = map(int, input().split())

flag = 0
for x in range(-999, 1000):
    for y in range(-999, 1000):

        if a*x + b*y == c:
            if d*x + e*y == f:
                ans_x = x
                ans_y = y
                flag = 1
                break
    if flag:
        break
print(ans_x, ans_y)
