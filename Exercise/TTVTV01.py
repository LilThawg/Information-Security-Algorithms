import math

def number_to_array (a,w,p):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    arr = []
    tmp = a
    for i in range(t):
        x = pow(2, ((t - 1 - i) * w))
        arr.append(tmp // x)
        tmp = tmp % x
    return arr

if __name__ == '__main__':
    p,W,a = map(int, input().split())
    # p = 2147483647
    # W = 8
    # a = 38762497
    res = str(number_to_array(a,W,p))
    print("A= "+res.replace(', ','   '))


