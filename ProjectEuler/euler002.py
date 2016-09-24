#!/usr/bin/env python3

'''
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

import numpy
mat = numpy.matrix

def euler002(n):
    sum = 0
    C = mat([[0,1], [1,1]])
    a = mat([[1], [2]])
    while a[1,0] <= n:
        a = C*a
        if a[0,0]%2 == 0:
            sum += a[0,0]
    return sum   

def main():
    n = 4000000
    result = euler002(n)
    print("euler project no.2: ", result)

main()
