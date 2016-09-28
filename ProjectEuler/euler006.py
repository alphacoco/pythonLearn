#!/usr/bin/env python3

'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def euler006(n):
	sumOfSquare = sum([x*x for x in range(1, n+1)])
	squareOfSum = sum([x for x in range(1, n+1)]) ** 2
	return squareOfSum - sumOfSquare

def main():
	n = 100
	result = euler006(n)
	print("euler project no.6: ", result)

main()