#!/usr/bin/python3
""" Script that write the minimum operations for a Copy All and Paste file """

def minOperations(n):
    if type(n) != int or n < 2:
        return 0

    minOps = 0
    i = 2
    while i <= n:
        while n % i == 0:
            minOps += i
            n //= i
        i += 1

    return minOps
