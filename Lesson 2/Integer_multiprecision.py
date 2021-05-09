# Alogorithm 04
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
if __name__ == '__main__':
    a = [0,11,173,248]
    b = [0,1,226,64]
    print(Integer_multiprecision(a,b))
