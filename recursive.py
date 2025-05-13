#!/usr/bin/env python3

def sum_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum_recursive(n-1)

n = sum_recursive(3)
print(n)
