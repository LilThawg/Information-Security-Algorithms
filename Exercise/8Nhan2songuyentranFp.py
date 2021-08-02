# Nhân hai số nguyên lớn trên trường hữu hạn
import math
def convert_uv_to_u_v(uv):
    bin_uv = str(bin(uv)[2:])
    if len(bin_uv) < 16 :
        bin_uv = "0"*(16-len(bin_uv))+bin_uv
    u = int(bin_uv[:8],2)
    v = int(bin_uv[8:],2)
    return u,v
def Integer_multiprecision (a, b, w=8, p=2147483647):
    a = a[::-1]
    b = b[::-1]
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    c = [0]*2*t
    for i in range(t):
        u = 0
        for j in range(t):
            uv = c[i+j]+a[i]*b[j]+u
            u,v = convert_uv_to_u_v(uv)
            c[i+j] = v
        c[i+t] = u
    return c[::-1]

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
       p,W,a,b = map(int, input().split())
       a = number_to_array(a)
       b = number_to_array(b)
       res = str(Integer_multiprecision(a,b,W,p))
       print("c=a.b="+res.replace(', ','   '))

'''
Input:
2147483647 8 524647 32549

Output:
c=a.b=[0   0   0   3   249   218   76   227]
'''
