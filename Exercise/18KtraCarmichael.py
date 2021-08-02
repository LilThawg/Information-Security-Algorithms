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
    elif n < 2 : return False
    b = 2
    while(b < n):
        if math.gcd(b,n) == 1 :
            if pow(b,n-1,n) != 1 :
                return False
        b+=1
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if isCarmichael(n):
            print(f'{n} la so Carmichael')
        else:
            print(f'{n} khong phai so Carmichael')


'''
Input:
2
561
22

Output:
561 la so Carmichael
22 khong phai so Carmichael
'''
