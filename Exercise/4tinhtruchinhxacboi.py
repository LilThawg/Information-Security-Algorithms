# Tính trừ chính xác bội
import math

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

if __name__ == '__main__':
    p,W,a,b = map(int, input().split())
    a = number_to_array(a)
    b = number_to_array(b)
    res = str(Multiprecision_subtraction(a,b,W,p))
    res = res.split(",")
    t = "c=a-b="+res[0]+","+res[1]+" "*2+res[2]+" "*2+res[3]+" "*2+res[4]
    print(t)


'''
Input:
2147483647 8 38762497 568424364

Output:
c=a-b=(1, [224   110   0   85])
'''
