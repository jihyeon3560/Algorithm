A, B, C, M = map(int, input().split())

work = 0
fatigue = 0
t = 0
while t < 24:
    t += 1
    if A > M:
        break
    if fatigue + A <= M:
        work += B
        fatigue += A
    else:
        if fatigue - C >= 0:
            fatigue -= C
        else:
            fatigue = 0

print(work)