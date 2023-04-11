def counting_sort(A,k): 
    n = len(A)
    C = [0] * k   
    B = [-1] * n
    for x in A:
        C[x]+=1
    for i in range (1,k):
        C[i] =C[i] +C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] =A[i]
        C[A[i]] -=1
    for i in range(n):
        A[i] = B[i]
     #   print(A[i])
    return B

A = [5,3,2,2,2,5,5,5,1,0,0,1,0,0,4,4,4]
print(counting_sort(A,6))
