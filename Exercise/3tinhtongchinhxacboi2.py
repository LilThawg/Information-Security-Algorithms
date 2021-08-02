# Tính tổng chính xác bội 2
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

if __name__ == '__main__':
    p,W = map(int, input().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    res = str(Multiprecision_addition(a,b,W,p))
    res = res.split(",")
    t = "A+B="+res[0]+","+res[1]+" "*2+res[2]+" "*2+res[3]+" "*2+res[4]
    print(t)
'''
Input:
2147483647 8
2    79   120     1
33   225   119   172

Output:
A+B=(0, [36    48   239   173])
'''
