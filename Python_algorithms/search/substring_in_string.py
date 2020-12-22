# naive algorithm
def find(text: str, word: str):
	""" Find sub-string in string O(N*M) """
	n = len(text)
	len_word = len(word)
	answer = ''
	for i in range(n):
		if text[i: i + len_word] == word:
			answer += (str(i) + ' ')
	return answer if answer == '' else -1

# example
# string = 'abacabadaba'
# w = 'aba'
string = input("Enter the text: ")
w = input('Enter the word to find: ')
print(find(string, w))


# Its quient long.
# We will implement Knuth-Morris-Pratt algorithm
