# Recursive function
def f(n: int):
	""" Calculate factorial 
	    Only for integer numbers.
	    Doesn't calculate the Gamma function """
	assert n >= 0 "Number must not be negative. I dont know the gamma function"
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return f(n - 1) * n


number = int(input("Input: "))
print(f(number))

# Using for loop
def f(n: int):
	if n < 0:
		return "I dont know the gamma function"
	if n == 0 or n == 1:
		return 1
	facto = 1
	while n > 1:
		fact *= n
		n -= 1
	return facto

# number = int(input("Input: "))
# print(f(number))
