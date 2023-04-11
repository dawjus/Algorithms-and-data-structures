def merge_list(T1, T2):   # moze byc stabilne i nawet jest
    n1 = len(T1)
    n2 = len(T2)
    T = [None for _ in range(n1+n2)]
    n = len(T)
    l = r = i = 0
    while l < n1 and r < n2:
        if T1[l] <= T2[r]:
            T[i] = T1[l]
            i+=1
            l+=1
        elif T1[l] > T2[r]:
            T[i] = T2[r]
            i+=1
            r+=1
    while l < n1:
        T[i]=T1[l]
        l+=1
        i+=1
    while r < n2:
        T[i]=T2[r]
        r+=1
        i+=1
    return T

def merge(T, l, r):

    if l >= r:
        return None
    elif l+1 ==r:
        return [T[0]]
    else:
        n = len(T)
        mid = n//2
        left = T[:mid]
        right = T[mid:]
        T1 = merge(left, 0, mid)
        T2 = merge(right, mid, len(T))
        T = merge_list(T1, T2)
        return T

T = [2, 4, 1, 7, 8, 4, 5]
print(T)
print(merge(T, 0, len(T)))
