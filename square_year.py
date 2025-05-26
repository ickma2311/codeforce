from sys import stdin

input = stdin.readline


def is_square_year(year: int) -> bool:
    if year**0.5 == int(year**0.5):
        return int(year**0.5)
    else:
        return -1


for _ in range(int(input())):
    year = int(input())
    if is_square_year(year) >= 0:
        print(is_square_year(year), 0)
    else:
        print(-1)
