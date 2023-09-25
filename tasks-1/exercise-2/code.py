def reverseList(arr, n, m):
    n = 0 
    m = len(arr) - 1
    while n < m:
        arr[n], arr[m] = arr[m], arr[n]
        n += 1
        m -= 1
    return arr