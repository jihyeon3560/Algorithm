lst = []
for i in range(1, 10001):
    s = 0
    n = i
    while n > 0:
        s += n % 10
        n //= 10
    s += i
    lst.append(s)
    if i not in lst:
        print(i)
