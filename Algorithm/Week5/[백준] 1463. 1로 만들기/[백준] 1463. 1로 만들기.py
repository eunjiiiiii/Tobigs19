n = int(input())
cnt = {1: 0}
def calc(x):
    if x in cnt.keys():
        return cnt[x]
    if (x % 3 == 0) and (x % 2 == 0):
        return min(calc(x//3) + 1, calc(n//2) + 1)
    elif x % 3 == 0:
        return min(calc(x//3)+1, calc(x-1)+1)
    elif x % 2 == 0:
        return min(calc(x//2)+1, calc(n-1)+1)
    else:
        cnt[x] = calc(x-1) + 1
    return cnt[x]

print(calc(n))
