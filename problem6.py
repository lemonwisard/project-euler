
x = [2]

for i in range(3,105000,2):
	is_prime=True
	for j in x[1:]:
		if i%j==0:
			is_prime=False
	if is_prime==True:
		x.append(i)
print(x)

tmp = []
for i in x:
	tmp.append(str(i))

print(tmp[10000])


