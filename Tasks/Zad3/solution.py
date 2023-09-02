def ice_cream( T ):
    n = len(T)
    T.sort(reverse = True)
    counter = 0
    pointer = 0
    sum_ = 0
    while T[pointer] > counter and pointer < n:
        sum_ += T[pointer]
        sum_ -= counter
        counter +=1
        pointer+=1
    return sum_
