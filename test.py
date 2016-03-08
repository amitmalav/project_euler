i = 2;
num1 = 1
num2 = 2
n = input("Inter n: ")
if n == 1:
	print(num1)
else:
	while i < n:
		tmp = num2
		num2 = num2 + num1
		num1 = tmp
		i += 1

	print(num2)