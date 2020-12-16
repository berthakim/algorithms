a = [4, 3, 2, 5, 1, 0, 1, 2, 2, 2, 6, 3, 8, 9, 10, 12, 6, 8]
n = len(a)
for i in range(n):
	for j in range(1, n-i):
		if a[i+j] < a[i]:
			a[i+j], a[i] = a[i], a[j+i]
print(a)
