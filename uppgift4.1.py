
x = []
for a in range(100,1000,1):
	x.append(a)

z = []
for b in range(100,1000,1):
	z.append(b)
a = []
for i in z:
	for j in x:
		a.append(i*j)
a.sort()
a.reverse()

q = []
for j in a:
	text=str(j)
	if text[3:] == text[:3][::-1]:
		print(text)
		break
