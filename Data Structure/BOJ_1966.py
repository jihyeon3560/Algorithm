T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    index = [i for i in range(n)]
    target = index[m]
    cnt = 0

    while priority:
        if priority[0] == max(priority):
            cnt += 1
            if index[0] == target:
                print(cnt)
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))