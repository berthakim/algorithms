# Collatz conjecture. Très très basique

# ---------------
# first solution:
#----------------
n = int(input("Enter a digit: "))

while n > 1:
	n = n // 2 if n % 2 == 0 else n * 3 + 1
	print(n, end=" ")
print()

# -------------------------
# using generator function:
# -------------------------
def collatz(n):
	while n > 1:
		yield n
		n = n // 2 if n % 2 == 0 else n * 3 + 1

# ----------------------------------------------------
# if we need to save the values for example in a list:
# ----------------------------------------------------
def collatz_list(n):
	collatz_sequence = []
	while n > 1:
		collatz_sequence.append(n)
		n = n // 2 if n % 2 == 0 else n * 3 + 1
	print(*collatz_sequence, 1)


# -----------------
# A byte of theory:
# -----------------
'''
On September 8, 2019, Terence Tao published a proof showing that 
Collatz's conjecture is at least "almost" true "almost" for all numbers. 
And although Tao's result is not a complete proof of the hypothesis, 
it is a very serious breakthrough for a task that does not so easily
reveal all its secrets.

“I didn't expect to solve the problem completely,” said Tao, 
a mathematician at the University of California, Los Angeles. 
"But I did more than I expected."

Collatz puzzle

Lothar Collatz probably put forward the hypothesis of the same name 
in the 1930s. The challenge sounds like a party trick. Take any number. 
If it's even, divide it by two. If odd, multiply by three, add one. 
A new number will be obtained. Apply the same rules for him. 
The hypothesis tells what happens if you persistently repeat this process.

Intuition dictates that the starting number affects the final result. 
Perhaps some numbers will eventually decrease to 1. Perhaps other numbers 
will increase indefinitely.

However, Collatz predicted that this was not the case. He suggested that 
if you start with a positive integer and repeat the specified sequence 
long enough, then from any seed you will come to 1. And when you come to 1, 
you will fall into the trap of the rules of the hypothesis, 
and you will enter an endless loop: 1, 4 , 2, 1, 4, 2, 1, and so on, ad infinitum.
source: https://habr.com/ru/post/482812/
'''
