#!/usr/bin/env python3

"""
Author          : Neda Peyrone
Create Date     : 15-06-2020
File            : coin_change.py
"""


def coin_change(n, coins):
    ans = [-1] * (n + 1)
    ans[0] = 0
    idx = 1

    while idx <= n:
        ans[idx] = 1e9
        for c in range(len(coins)):
            if idx - coins[c] >= 0:
                ans[idx] = min(ans[idx], 1 + ans[idx - coins[c]])
        idx += 1

    return ans[n]


if __name__ == '__main__':
    result = coin_change(6, [1, 3, 4])
    print(f"result: {result}")
