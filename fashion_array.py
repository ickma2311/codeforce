# Problem: https://codeforces.com/contest/2110/problem/A
from sys import stdin
from typing import List

input = stdin.readline


def backtrack(arr: List[int], lens: List[int]):
    if len(arr) == 0:
        return
    if (arr[0]+arr[-1]) % 2 == 0:
        return lens.append(len(arr))
    arr_1 = arr[1:]
    arr_2 = arr[:-1]
    backtrack(arr_1, lens)
    backtrack(arr_2, lens)
    return lens


n = int(input())
for _ in range(n):
    len_ = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    lens = []
    backtrack(arr, lens)
    print(len_-max(lens))
