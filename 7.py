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
while i < n:
	if is_prime(v):
		i+= 1
		if i == n:
			break
	v = v + 2
	if is_prime(v):
		i+= 1
		if i == n:
			break
	v = v + 4

print(v)