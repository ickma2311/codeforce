# Problem: https://codeforces.com/contest/2114/problem/B

from sys import stdin

input = stdin.readline


def check_possibility(s: str, k: int) -> bool:

    count_0 = sum(1 for i in s if i == '0')
    count_1 = sum(1 for i in s if i == '1')

    # first let us check after the k good pairs,
    # how many 0s and 1s we need

    j = len(s)-k*2
    # now we need j//2 0 and j//2 1

    count_0 -= j//2
    count_1 -= j//2

    if count_0 < 0 or count_1 < 0:
        return False

    # now we only have paris, let us check
    # to generate good pairs,
    # we need even 0s and even 1s
    return count_0 % 2 == 0 and count_1 % 2 == 0


for _ in range(int(input())):
    _, k = input().strip().split()
    s = input().strip()
    if check_possibility(s, int(k)):
        print("YES")
    else:
        print("NO")
