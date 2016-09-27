#!/usr/bin/env python3
 
'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
# Lowest Common Multiple(LCM)
# Greatest Common Divisor(GCD)

'''
# the Recursion way
def euler005(n):
	L = [x for x in range(1,n+1)]
	return euler005Helper(L, 0, len(L) - 1)

def euler005Helper(L, low, high):
	if low == high:
		return L[low]
	return lcm(euler005Helper(L, low, high-1), L[high])

'''

# the iteration way
def euler005(n):
	y = 1
	for x in range(1, n+1):
		y = lcm(x, y)
	return y

def lcm(u, v):
	if u < v:
		u, v = v, u
	return u*v // gcd(u,v)

def gcd(u,v):
	if v == 0:
		return u
	return gcd(v, u%v)


def main():
	n = 20
	result = euler005(n)
	print("euler project no.5: ", result)

main()
