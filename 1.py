def gcd(a, b):
	if(b == 0):
		return a
	return gcd(b, a%b)
	# while(b != 0):
	# 	tmp = a % b
	# 	a = b
	# 	b = tmp
	# return a
def hardcode():
	count = 0
	for num in range(1, 1000):
		if (num % 3 == 0) or (num % 5 == 0):
			count += num
	return count


#we can also write it as some of (S3+S5-S15) ie.


# count = 3*int(999/3)*(1 + int(999/3))/2 + 5*int(999/5)*(1 + int(999/5))/2 - 15*int(999/15)*(1 + int(999/15))/2
# print count



def generalsum(a, b, below):
	below = below - 1
	lcm = (a/gcd(a,b))*b
	count = a*int(below/a)*(1 + int(below/a))/2 + b*int(below/b)*(1 + int(below/b))/2 - lcm*int(below/lcm)*(1 + int(below/lcm))/2
	return count

if __name__ == "__main__":
	print "a is "
	a = input()
	print "b is "
	b = input()
	print "range is "
	below = input()
	print "sum is:",generalsum(a, b, below)
