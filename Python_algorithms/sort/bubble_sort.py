# complexity: O(n^2)
# for every sort algorithm
# mesure the time spent to sort

def bubble_sort(a):
	''' Bubble sort '''
	n = len(a)
	for i in range(n - 1):
		# in (0, n-i-1), -i = because on eatch iteration
		# the last element are already sorted so
		# so there's no need to check "if >" again
		for j in range(0, n-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a


def insert_sort(a):
	pass


def selection_sort(a):
	pass


def test_algorithm(sort_algorithm):
	print("Test for:", sort_algorithm.__doc__)
	print("Test 1: ", end='')
	a = [5, 4, 3, 2, 1]
	a_sorted = [1, 2, 3, 4, 5]
	#  call sorting algorithm to change list "a"
	sort_algorithm(a)  # "a" changed now (sorted)
	# comparation of 2 lists is len(a) operations!
	print("Ok" if a == a_sorted else "fail")

	print("Test 2: ", end='')
	a = [8, 3, 3, 6, 3]
	a_sorted = [3, 3, 3, 6, 8]
	sort_algorithm(a)
	print("Ok" if a == a_sorted else "fail")

	print("Test 3: ", end='')
	a = [-1, 4, 5, 2, 1]
	a_sorted = [-1, 1, 2, 4, 5]
	sort_algorithm(a)
	print("Ok" if a == a_sorted else "fail")


if __name__ == "__main__":
	test_algorithm(bubble_sort)
	# test_algorithm(insert_sort)
	# test_algorithm(selection_sort)
