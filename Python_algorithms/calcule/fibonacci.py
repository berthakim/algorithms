m = {0: 0, 1: 1}

def fib(n):
	""" 
	Fibonacci number optimized by a dictionnary. 
	Application of recursion with storing already calculated values. 
	This approach turns exponential computation time into linear time, 
	which spends more memory.
	Possible stack overflow with large numbers
	"""
	if n in m:
		return m[n]
	m[n] = fib(n - 1) + fib(n - 2)
	return m[n]


number = int(input("Input: "))
print(f'{number}th fibonacci number is: {fib(number)}')


# Dynamic programming
def fib(n):
	"""
	Works fast for small n. Linear time computation
	We do not need all the previous results, but only the last two. 
	As an alternative to the recursive algorithm, instead of starting 
	at fib (n) and walking backward, one can start at fib (0) 
	and walk forward. The following function has linear execution 
	time and fixed memory usage. In practice, the speed of the 
	solution will be even higher, since there are no recursive 
	function calls and associated work.
	"""
	f0, f1 = 0, 1
	for i in range(n):
		f0, f1 = f1, f0 + f1
	return f0
