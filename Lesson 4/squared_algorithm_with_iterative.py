def squared_algorithm_with_iterative (a,k,n):
    k = bin(k)[2:][::-1]
    k = list(k)
    t = len(k)
    b = 1
    A = a
    if k[0] == '1':
        b = a
    for i in range(1,t):
        A = A*A % n
        if k[i] == '1':
            b = A*b % n
    return b

print(squared_algorithm_with_iterative(25,705,3542))

