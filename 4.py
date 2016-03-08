
def pal(num):
	str1 = str(num)
	str2 = str1[::-1]
	if (str1 == str2):
		return 1
	return 0

pal_list = []
for i in range(999, 0, -1):
	for j in range(999, 0, -1):
		num = i*j
		if pal(num):
			pal_list.append(num)

print(max(pal_list))