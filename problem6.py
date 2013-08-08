
x = [1,2]

for i in range(3,10002,2):
	is_prime=True
	for j in x[1:]:
		if i%j==0:
			is_prime=False
	if is_prime==True:
		x.append(i)

for i in x:
	x.append(str(i))
	print(x)

