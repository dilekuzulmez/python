#! /usr/bin/env python
# -*- coding: UTF-8 -*-
fib1 = 1
fib2 = 1
n = input("Kacinciyi hesapyalayalim: ")
for i in range(3,n+1):
    fib = fib1+fib2
    fib1, fib2 = fib2, fib
print fib
