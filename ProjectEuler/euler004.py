#!/usr/bin/env python3

'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def euler004(n):
	m1 = pow(10, n-1) 
	m2 = pow(10, n)
	max_Palindrome = [0, 0, 0]
	for i in range(m1, m2):
		for j in range(m1, m2):
			if isPalindrome(i*j):
				if i*j > max_Palindrome[2]:
					max_Palindrome = [i, j, i*j]
	return max_Palindrome

def isPalindrome(n):
	s = str(n)
	return isPalindromeHelper(s, 0, len(s)-1)

def isPalindromeHelper(s, low, high):
	if low > high:
		return True
	elif s[low] != s[high]:
		return False
	else:
		return isPalindromeHelper(s, low+1, high-1)

def main():
	n = 3
	result = euler004(n)
	print("euler project no.4 ", result[2])

main()