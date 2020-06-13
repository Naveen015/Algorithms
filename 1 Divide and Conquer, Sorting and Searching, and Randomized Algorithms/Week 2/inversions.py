def sort_and_count(A):
	if len(A)<=1:
		return A,0
	else :
		(B,x) = sort_and_count(A[:len(A)//2])
		(C,y) = sort_and_count(A[len(A)//2:])
		(D,z) = count_split_inv(B,C)
		return D,x+y+z

def count_split_inv(B,C):
	D = []
	inversions = 0
	while B and C:
		if B[0] <= C[0]:
			D.append(B[0])
			B.remove(B[0])
		else:
			D.append(C[0])
			C.remove(C[0])
			inversions += len(B)
	D += B or C
	return D, inversions

if __name__ == "__main__":
	with open('IntegerArray.txt','r') as f:
		A = []
		for line in f:
			A.append(int(line))	
	print(sort_and_count(A)[1])
