def counting_sort(a):
    """
    Counting sort of a list
    Only for range of digits from 0 to 10
    O(n) (for big ranges complexity will be:
    O(n+k), k - number of elements in range)
    """
    n = len(a)
    diap = 10
    f = [0] * diap
    # frequency list
    for i in a:
        f[i] += 1
    a = []
    for k in range(diap):
        a += [k] * f[k]
    return a


a = [2, 5, 6, 1, 2, 8, 4, 9, 9, 6, 1, 2, 4, 7, 6, 5, 4, 3, 9, 8, 0]
print(counting_sort(a))
