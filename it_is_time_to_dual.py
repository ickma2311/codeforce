# Problem: https://codeforces.com/contest/2109/problem/A
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    n_players = int(input())
    reports = input().split()

    winners = defaultdict(int)
    losers = defaultdict(int)

    #  1 0 0 1
    for i in range(n_players-1):
        winner = None
        loser = None
        if reports[i] == '1':
            if i == 0 or i == n_players-1:
                winner = i
                loser = i+1
            else:  # when between, if it loses before, then we trust it wins this time
                if losers[i] == 1:
                    winner = i
                    loser = i+1
            #    if it wins before, we don't know what to do

        # we can only trust 0
        if reports[i] == '0':
            loser = i
            winner = i+1

        winners[winner] += 1
        losers[loser] += 1

    # let us check winner and loser reports
    for k, v in winners.items():
        if k is None:
            continue
        if v == 1 and reports[k] == '0':
            print("Yes")
            break
    else:

        for k, v in losers.items():
            if k is None:
                continue
            if v == 1 and (k == 0 or k == n_players-1) and reports[k] != '0':
                print("Yes")
                break
            if v == 2 and reports[k] == '1':
                print("Yes")
                break
        else:
            print("No")
