
a = 1
b = 1

c = 1

for a in range(1,501):

	a = a+1
	
	for b in range(1,501):

		b = b+1
		a


	for c in range(1,501):

		c = c+1

	if a**2+b**2 == c**2 and a+b+c == 1000:
		print (a)
		print (b)
		print (c)
		print (" ")
		break
