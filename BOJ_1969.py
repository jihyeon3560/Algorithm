import sys

N, M = map(int, sys.stdin.readline().split())
dna = [''] * N
for i in range(N):
    dna[i] = sys.stdin.readline().strip()

ans = 0
s = ''
for i in range(M):
    cnt_a = cnt_t = cnt_g = cnt_c = 0
    for j in range(N):
        if dna[j][i] == 'A':
            cnt_a += 1
        elif dna[j][i] == 'T':
            cnt_t += 1
        elif dna[j][i] == 'G':
            cnt_g += 1
        elif dna[j][i] == 'C':
            cnt_c += 1

    tmax = max(cnt_a, cnt_t, cnt_g, cnt_c)
    ans += N - tmax
    if tmax == cnt_a:
        s += 'A'
    elif tmax == cnt_t:
        s += 'T'
    elif tmax == cnt_g:
        s += 'G'
    elif tmax == cnt_c:
        s += 'C'

print(s)
print(ans)