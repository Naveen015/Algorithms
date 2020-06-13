def karatsuba_mult(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n=max(len(str(x)),len(str(y)))

		n2= n // 2

		a = x // (10**n2)
		b = x % (10**n2)
		c = y // (10**n2)
		d = y % (10**n2)

		z2=karatsuba_mult(a,c)
		z0=karatsuba_mult(b,d)
		z1=karatsuba_mult((a+b),(c+d))

		ans=(10**(2*n2))*z2 + (10**n2)*(z1-z0-z2) + (z0)
		return ans

x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba_mult(x,y))
