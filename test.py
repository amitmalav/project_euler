def gcd(a, b):
	if(b == 0):
		return a
	return gcd(b, a%b)
	# while(b != 0):
	# 	tmp = a % b
	# 	a = b
	# 	b = tmp
	# return a

if __name__ == "__main__":
	a = input()
	b = input()
	print gcd(a, b)