n = int(input())
ans = 0
coin = [500,100,50,10]

for i in range(0,4):
    ans += n // coin[i]
    n %= coin[i]

print(ans)