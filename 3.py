import math
n = input()
i = 2
while(i <= int(math.sqrt(n))):
	if n % i:
		i += 1
	else:
		n /= i
print(n)