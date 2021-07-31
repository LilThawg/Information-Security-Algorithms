# Alogorithm 03
import math

def Multiprecision_addition(a, b, w=8, p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    c = [''] * t
    e = 0
    for i in range(t):
        c[t-1-i] = (a[t-1-i] + b[t-1-i] + e) % (2**w)
        if a[t-1-i] + b[t-1-i] + e >= 2**w :
            e = 1
        else :
            e = 0
    return e,c

def Multiprecision_subtraction(a, b, w=8, p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    c = [''] * t
    e = 0
    for i in range(t):
        c[t-1-i] = (a[t-1-i] - b[t-1-i] - e) % (2**w)
        if a[t-1-i] - b[t-1-i] - e < 0 :
            e = 1
        else :
            e = 0
    return e,c

def Subtraction_in_Fp (a,b,p):
    e, c = Multiprecision_subtraction(a, b)
    while array_to_number(c) >= array_to_number(p):
        e, c = Multiprecision_subtraction(c, p)
    return c

def number_to_array (a,w=8,p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    arr = ['']*t
    tmp = a
    sum = 0
    for i in range(t):
        x = pow(2, ((t - 1 - i) * w))
        arr[i] = tmp // x
        sum += arr[i] * x
        tmp = a - sum
    return arr

def array_to_number(arr,w=8,p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    a = 0
    for i in range(t):
        x = pow(2, ((t - 1 - i) * w))
        a += arr[i] * x
    return a

if __name__ == '__main__':
    a = number_to_array(38762497)
    b = number_to_array(568424364)
    p = number_to_array(2147483647)
    print(Subtraction_in_Fp(a,b,p))
