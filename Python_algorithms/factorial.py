def f(n: int):
	assert n >= 0
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return f(n - 1) * n


number = int(input("Input: "))
print(f(number))
