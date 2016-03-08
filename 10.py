import math
def is_prime(n):
	i = 2
	while i <= math.sqrt(n):
		if(n%i == 0):
			return 0
		i+= 1
	return 1

i = 2
v = 5
n = input()
sum1 = 5
while v < n:
	if is_prime(v):
		sum1 += v 
	v = v + 2
	if is_prime(v):
		if(v < n):
			sum1 += v
	v = v + 4

print(sum1)