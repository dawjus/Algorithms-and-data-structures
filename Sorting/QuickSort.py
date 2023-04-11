def Partition(T, begin, end):
    pivot = T[end]
    j = begin - 1
    for i in range(begin, end):
        if T[i] < pivot:
            j += 1
            T[i], T[j] = T[j], T[i]
    T[j+1], T[end] = pivot, T[j+1]
    return j+1

def Quicksort(T, begin, end):
    n = end - begin + 1
    if n == 1:
        return T[begin]
    if end > begin:
        pivot = Partition(T, begin, end)
        Quicksort(T, begin, pivot-1)
        Quicksort(T, pivot+1, end)
        return T

K = [1,2,0,5,-2,-9]
print(Quicksort(K, 0, len(K)-1))
