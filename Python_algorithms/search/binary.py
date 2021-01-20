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
	'''
	length = n
	left = 0
	while left <= length:
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


# lst = [1, 2, 3, 4, 6, 7, 8, 10, 12, 14]
# length = len(lst)
# left = 0
# x = 8
# print(binary_recursive(lst, left, length, x))
# output: 6

# test binary search algorithm
def test_algorithm(algorithm):
	print("Test for:", algorithm.__doc__)

	print("Test 1: ", end='')
	arr1 = [1, 2, 3, 4, 6, 7, 8, 10, 12, 14]
	n1 = len(arr1)
	x1 = 8
	x1_founded = 6  # INDEX of element wich we search (x1)

	algorithm_response = algorithm(arr1, n1, x1)
	print(f'Ok' if algorithm_response == x1_founded else 'Fail', end='\n\n')

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
