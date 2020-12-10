def selection_sort(a: list):
	""" Selection sort """
	n = len(a)
	for i in range(n):
		for j in range(1, n-i):
			if a[i+j] < a[i]:
				a[i+j], a[i] = a[i], a[j+i]
	return a

def insertion_sort(a: list):
	""" Insertion sort """
	n = len(a)
	for i in range(n):
		for j in range(1, n-i):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
	return a

def bubble_sort(a: list):
	""" Bubble sort """
	n = len(a)
	for i in range(n - 1):
		for j in range(0, n-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a

def testing_algorithms(sorting_algorithm):
	print("Testing algorithm:", sorting_algorithm.__doc__)

	print("Test 1 - ", end='')
	a1 = [5, 4, 3, 2, 1]
	a_sorted = [1, 2, 3, 4, 5]
	sorting_algorithm(a1)
	print("Ok" if a1 == a_sorted else 'fail')

	print("Test 2 - ", end='')
	a2 = [1, 0, 0, 0, 0, 0]
	a_sorted = [0, 0, 0, 0, 0, 1]
	sorting_algorithm(a2)
	print("Ok" if a2 == a_sorted else 'fail')

	print("Test 3 - ", end='')
	a3 = [5, 4, 3, 3, 3, 2, 2, 1]
	a_sorted = [1, 2, 2, 3, 3, 3, 4, 5]
	sorting_algorithm(a3)
	print("Ok" if a3== a_sorted else 'fail')

	print("Test 4 - ", end='')
	a4 = []
	a_sorted = []
	sorting_algorithm(a4)
	print("Ok" if a4== a_sorted else 'fail')

	print("Test 5 - ", end='')
	a5 = [6]
	a_sorted = [6]
	sorting_algorithm(a5)
	print("Ok" if a5== a_sorted else 'fail')

	print("Test 6 - ", end='')
	a6 = [4, 3, 2, 5, 1, 0, 1, 2, 2, 2, 6, 3, 8, 9, 10, 12, 6, 8]
	a_sorted = [0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 6, 8, 8, 9, 10, 12]
	sorting_algorithm(a6)
	print("Ok" if a6 == a_sorted else 'fail')
	print()


if __name__ == "__main__":
	testing_algorithms(selection_sort)
	testing_algorithms(insertion_sort)
	testing_algorithms(bubble_sort)
