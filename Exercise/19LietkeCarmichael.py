import math
def isPrime(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def isCarmichael(n):
    if isPrime(n) :
        return False
    elif n < 2 or n % 2 == 0 : return False
    b = 2
    while(b < n):
        if math.gcd(b,n) == 1 :
            if pow(b,n-1,n) != 1 :
                return False
        b+=1
    return True

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(2,n+1):
        if isCarmichael(i) :
            arr.append(i)
    res = str(arr).strip('[]').replace(", ", "   ")
    print(res)


