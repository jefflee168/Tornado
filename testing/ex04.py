# -*- coding: utf-8 -*-

def demo():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3
    print("fourth")
    yield 4
    print("fifth")
    yield 5

for i in demo():
    print(i)