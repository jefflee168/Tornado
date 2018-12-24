# -*- coding: utf-8 -*-

def demoIterator():
    print("I'm in the first call of next()")
    yield 1
    print("I'm in the second call of next()")
    yield 2
    print("I'm in the third call of next()")
    yield 3
    print("I'm in the fourth call of next()")
    yield 4
    print("I'm in the fifth call of next()")
    yield 5

for i in demoIterator():
    print(i)