def SelectionSort(T):
    n = len(T)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if T[mini] > T[j]:
                mini = j
        T[i], T[mini] = T[mini], T[i]
    return T

T = [4, 2, 1, 5, 4, 5, 7, 3]
print(T)
print(SelectionSort(T))