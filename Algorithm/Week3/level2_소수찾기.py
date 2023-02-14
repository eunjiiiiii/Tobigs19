from itertools import permutations
def solution(number):
    a = set()
    for i in range(len(number)):
        a |= set(map(int, map("".join, permutations(list(number), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)