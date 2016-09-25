#!/usr/bin/env python3

'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

from math import floor
from math import sqrt

def euler003(n):
	return max(euler003Helper(n))

def euler003Helper(n):
	for x in range(2, int(sqrt(n))+1):
		if n%x == 0:
			u = euler003Helper(n//x)
			return [x] + u
	return [n]

def main():
	n = 600851475143
	result = euler003(n)
	print("euler project no.3 ", result)

main()
