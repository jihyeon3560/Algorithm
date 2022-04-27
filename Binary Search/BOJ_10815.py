def binary_search(num):
    l = 0
    r = N-1
    while l <= r:
        mid = (l+r)//2
        if cards[mid] == num:
            return 1
        elif cards[mid] < num:
            l = mid + 1
        else:
            r = mid -1
    return 0


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

cards.sort()
for num in numbers:
    print(binary_search(num), end = ' ')
