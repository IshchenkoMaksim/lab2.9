#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


@lru_cache
def non_rec_factorial(n=5):
    for i in range(1, n+1):
        n += i


@lru_cache
def rec_factorial(n=5):
    if n == 1:
        return 1
    return n + rec_factorial(n - 1)


print(timeit.timeit(stmt=non_rec_factorial, number=10000))
print(timeit.timeit(stmt=rec_factorial, number=10000))
