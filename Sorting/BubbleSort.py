def BubbleSort(T):
    n = len(T)
    for i in reversed(range(1, n)):
        for j in range(i):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T


T = [4, 2, 1, 9, 5, 4, 5, 7, 3, 0]
print(T)
print(BubbleSort(T))
