#!/usr/bin/env python3

def initB(A):
	B = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
	for i in range(9):
		for j in range(9):
			if A[i][j] != 0:
				B[i][j] = 1
	return B

def Bpointk(B, A, k):
	for i in range(9):
		for j in range(9):
			if A[i][j] == k:
				B = BpointkHelper(B, i, j)
				break
	return B

def BpointkHelper(B, i, j):
	for x in range(9):
		B[i][x] = 1
	for x in range(9):
		B[x][j] = 1
	for x in range(i//3 * 3, i//3 * 3 + 3):
		for y in range(j//3 * 3, j//3 * 3 +3):
			B[x][y] = 1

	return B

def printM(M):
	for i in range(9):
		for j in range(9):
			print(M[i][j], '  ', end = '')
		print()

def sumA(A):
	sum_A = 0;
	for i in range(9):
		for j in range(9):
			sum_A += A[i][j]
	return sum_A

def Apointk(A, B, k):
	while True:
		pre_sumA = sumA(A)
		for i in range(3):
			for j in range(3):
				count, index_i, index_j = ApointkHelper(B, i, j)
				if count == 1:
					A[index_i][index_j] = k
					B = BpointkHelper(B, index_i, index_j)					
		cur_sumA = sumA(A)
		if cur_sumA == pre_sumA:
			return A

def ApointkHelper(B, n, m):
	count, index_i, index_j = 0, -1, -1
	for i in range(n*3, n*3 + 3):
		for j in range(m*3, m*3 + 3):
			if B[i][j] == 0:
				count += 1
				index_i, index_j = i, j
	return count, index_i, index_j

def main():
	
	A = [[0, 5, 0, 8, 1, 0, 0, 0, 9],
		 [8, 0, 2, 0, 0, 7, 1, 0, 5],
		 [0, 6, 0, 3, 0, 0, 7, 0, 0],
		 [0, 0, 0, 0, 7, 0, 2, 0, 3],
		 [0, 1, 0, 5, 0, 6, 0, 8, 0],
		 [3, 0, 7, 0, 9, 0, 0, 0, 0],
		 [0, 0, 5, 0, 0, 3, 0, 1, 0],
		 [1, 0, 8, 7, 0, 0, 5, 0, 6],
		 [6, 0, 0, 0, 2, 5, 0, 7, 0]]
	
	k = 1
	while True:
		B = initB(A)
		B = Bpointk(B, A, k)
		A = Apointk(A, B, k)
		k = k % 9 + 1 
		if sumA(A) == 405:
			break
	printM(A)		

main()