import math
#if result wrong, please change c != 1 , example : x**2 + 9 instead of c = 1 or anything
def Pollard_Rho(n , seed = 2 , f = lambda x: x**2 + 1):
    a = seed
    b = seed
    Check = 0
    while Check == 0:
        a = f(a) % n
        b = f(f(b) %n) % n
        #print(a,b)
        d = math.gcd(abs(a-b),n)
        if 1 < d and d < n :
            Check = 1
            return d
        elif d == n :
            Check = 1
            return n

print(Pollard_Rho(455459))
