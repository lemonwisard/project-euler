
a = 250
b = 350

c = 400


print (a**2+b**2)
print (c**2)
	

while b**2-a**2 > c**2-b**2:
	a = a - 1
	c = c + 1
	print (a)
	print (b)
	print (c)
	print (" ")

while b**2-a**2 < c**2-b**2:
	b = b + 1
	c = c - 1
	print (a)
	print (b)
	print (c)
	print (" ")

if a**2+b**2==c**2:
	print (a)
	print (b)
	print (c)
	print (a*b*c)

else:
	print ("helt fel")



	


