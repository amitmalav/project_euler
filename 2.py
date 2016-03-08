count = 0
num1 = 1
num2 = 2
num3 = 2
while num3 < 4000000:
	if num2%2 == 0:
		count+= num2
	num3 = num2 + num1
	num1 = num2
	num2 = num3

print count