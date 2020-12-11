def fib(n):
	""" Fibonacci number """
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


# find_value_ofthis_fibonacci number
number = int(input("Input: "))
print(fib(number))
