N, K = map(int, input().split())

cnt = 0
for h in range(N+1):
    if h < 10:
        sh = '0' + str(h)
    else:
        sh = str(h)
    for m in range(60):
        if m < 10:
            sm = '0' + str(m)
        else:
            sm = str(m)
        for s in range(60):
            if s < 10:
                ss = '0' + str(s)
            else:
                ss = str(s)
            if str(K) in sh + sm + ss:
                cnt += 1

print(cnt)