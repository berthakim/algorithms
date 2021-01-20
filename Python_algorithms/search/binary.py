''' 
Inspired by description of binary algorithm in the book 
Introduction to algorithms by Thomas H. Cormen, p.41-42
'''

def binary_search(arr, n, x):
	''' Binary search
	    arr: list of values in wich we search
	    n: length of this list
	    x: element to find
	    If there is not x in the list then return -1
	    If there is only equals elements in a list and 
	    we are searching one of them 
	    then return any of indexes
	'''
	length = n
	left = 0
	while left < length:
		middle = (left + length) // 2
		if arr[middle] == x:
			return middle
		if arr[middle] > x:
			length = middle - 1
		else:
			left = middle + 1
	return -1

def binary_recursive(arr, left, length, x):
	""" Recursive binary search """
	if left > length:
		return "not-found"
	middle = (left +  length) // 2
	if arr[middle] == x:
		return middle
	if arr[middle] > x:
		return binary_recursive(arr, left, middle-1, x)
	if arr[middle] < x:
		return binary_recursive(arr, middle+1, length, x)


# test binary search algorithm
def test_algorithm(algorithm):
	print("Test for:", algorithm.__doc__)
	# args
	print("Test 1: ", end='')
	arr1 = [1, 2, 3, 4, 6, 7, 8, 10, 12, 14]
	n1 = len(arr1)
	x1 = 8
	x1_founded = 6  # INDEX of element wich we search (x1)
	# checking
	algorithm_response = algorithm(arr1, n1, x1)
	print(f'Ok' if algorithm_response == x1_founded else 'Fail', end='\n\n')

	# test 2
	print("Test 2: ", end='')
	arr2 = [0, 0, 1, 1, 1, 3, 4, 7, 7, 8, 8, 8, 10, 12, 14]
	n2 = len(arr2)
	x2 = 8
	x2_founded = [9, 10, 11]  # INDEX of element wich we search (x1)
	algorithm_response = algorithm(arr2, n2, x2)
	print(f'Ok' if algorithm_response in x2_founded else 'Fail', end='\n\n')

	# test 3
	print("Test 3: ", end='')
	arr3 = [1, 1, 1, 1, 1, 1]
	n3 = len(arr3)
	x3 = 1
	x3_founded = [0, 1, 2, 3, 4, 5]  # INDEX of element wich we search (x1)
	algorithm_response = algorithm(arr3, n3, x3)
	print(f'Ok' if algorithm_response in x3_founded else 'Fail', end='\n\n')

	# test 4
	print("Test 4: ", end='')
	arr4 = [0]
	n4 = len(arr4)
	x4 = 0
	x4_founded = 0 # INDEX of element wich we search (x1)
	algorithm_response = algorithm(arr4, n4, x4)
	print(f'Ok' if algorithm_response == x4_founded else 'Fail', end='\n\n')

	# test 5
	print("Test 5: ", end='')
	arr5 = []
	n5 = len(arr5)
	x5 = 8
	x5_founded = -1  # INDEX of element wich we search (x1)
	algorithm_response = algorithm(arr5, n5, x5)
	print(f'Ok' if algorithm_response == x5_founded else 'Fail', end='\n\n')

	# test 6
	print("Test 6: ", end='')
	arr6 = [1, 2, 3, 4, 6, 7, 8, 10, 12, 14]
	n6 = len(arr6)
	x6 = 5
	x6_founded = -1  # INDEX of element wich we search (x1)
	algorithm_response = algorithm(arr6, n6, x6)
	print(f'Ok' if algorithm_response == x6_founded else 'Fail', end='\n\n')

	# test 7 (4)
	print("Test 7: ", end='')
	arr7 = [0]
	n7 = len(arr7)
	x7 = 10
	x7_founded = -1  # INDEX of element wich we search (x1)
	algorithm_response = algorithm(arr7, n7, x7)
	print(f'Ok' if algorithm_response == x7_founded else 'Fail', end='\n\n')


# test recursive binary search algorithm
def test_algorithm_recurs(algorithm):
	print("Test for:", algorithm.__doc__)

	print("Test 1: ", end='')
	arr1 = [1, 2, 3, 4, 6, 7, 8, 10, 12, 14]
	length1 = len(arr1)
	left1 = 0
	x1 = 8
	x1_founded = 6  # INDEX of element wich we search (x1)

	algorithm_response = algorithm(arr1, left1, length1, x1)
	print(f'Ok' if algorithm_response == x1_founded else 'Fail')


if __name__ == "__main__":
	test_algorithm(binary_search)
	test_algorithm_recurs(binary_recursive)

# TODO: divide test_algorithm function by different types of test
# otherwise it's too long for being a optimal function
# and also add some tests for recursive binary search algorithm
