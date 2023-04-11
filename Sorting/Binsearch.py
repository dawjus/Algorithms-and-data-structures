def bin_search(T, val):
    b = 0
    e = len(T)-1
    while b < e:
        mid = (b + e) // 2
        if T[mid] > val:
            e = mid
        elif T[mid] < val:
            b = mid + 1
        else:
            return mid
    return -1


T = [1,2,9,12,14,19]
print(bin_search(T, 12))