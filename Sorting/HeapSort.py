def Left(i):
    return 2*i + 1


def Right(i):
    return Left(i) + 1


def Parent(i):
    return (i-1) // 2


def Heapify(T, n, i):
    left = Left(i)
    right = Right(i)
    if i >= n:
        return
    maxi = i
    if left < n and T[left] > T[maxi]:
        maxi = left
    if right < n and T[right] > T[maxi]:
        maxi = right
    if maxi != i:
        T[i], T[maxi] = T[maxi], T[i]
        Heapify(T, n, maxi)


def BuiltHeap(T):
    n = len(T)
    for i in range(Parent(n-1), -1, -1):
        Heapify(T, n, i)


def HeapSort(T):
    n = len(T)
    BuiltHeap(T)
    for i in range(n-1, -1, -1):
        print(T)
        T[0], T[i] = T[i], T[0]
        Heapify(T, i, 0)


T = [4, 2, 6, 1, 5, 3, 8, 2, 9]
print(T)
HeapSort(T)
print(T)


