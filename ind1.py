#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    def func(n, list_n):
        if n == 0:
            print(list_n[1], end='')
            for i in list_n[2:]:
                print(f'+{i}', end='')
            print('')
        else:
            x = list_n[len(list_n) - 1]
            if n >= x:
                for i in range(max(1, x), n + 1):
                    func(n - i, list_n + [i])


    num = int(input('Введите число, которое хотите разложить на слагаемые: '))
    func(num, [0])
