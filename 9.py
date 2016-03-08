import math
# for c in range(1000, 0, -1):
# 	for b in range(c-1, 0, -1):
# 		for a in range(b-1, 0, -1):
# 			if (a + b + c) == 1000 and (a**2 + b**2 == c**2):
# 				print a
# 				print b
# 				print c
# 				print(a*b*c)
# 				break


"""
a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
a + b + c = 1000;

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
2mn + 2m^2 = 1000;
2m(m+n) = 1000;
m(m+n) = 500;

m>n;

m= 20; n= 5;

a= 200; b= 375; c= 425;
"""

def pythtrip(l):
	for m in range(int(math.sqrt(l)), 0, -1):
		for n in range(m-1, 0, -1):
			if 2*m*(m + n) == l:
				a = 2*m*n
				b = m**2 - n**2
				c = m**2 + n**2
				product = a*b*c
				print "a =", a
				print "b =", b
				print "c =", c
				print "product is:", product

if __name__ == "__main__":
	print "give input"
	l = input()
	pythtrip(l)