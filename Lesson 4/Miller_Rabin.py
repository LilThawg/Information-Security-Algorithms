import random

def find_s_r(n):
    s = 1
    while True:
        if (n-1)%(2**s) != 0:
            break
        s+=1
    s = s-1
    r = (n-1)//(2**s)
    return s,r

def Miller_Rabin(n,t):
    s,r = find_s_r(n)
    Check = 1
    for i in range(1,t):
        a = random.randint(2,n-2)
        y = pow(a,r,n)
        if y != 1 and y != n-1:
            j = 1
            while j <= s-1 and y != n-1 :
                y = pow(y,2,n)
                if y == 1 : Check = 0
                j = j + 1
            if y != n-1 : Check = 0

    if Check ==0 : return 'Composite Number'
    else : return 'Prime Number'

if __name__ == '__main__':
    print('Miller-Rabin primality test')
    n = int(input('Enter number n you want check : '))
    t = int(input('Enter safety parameter t  :  '))
    print(Miller_Rabin(n,t))

