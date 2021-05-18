import random
def Fermat(n,t):
    Check = 1
    for i in range(t):
        a = random.randint(2,n-2)
        r = pow(a,n-1,n)
        if r != 1 :
            Check = 0
            break
    if Check == 0 : return 'Composite Number'
    else : return 'Prime Number'

if __name__ == '__main__':
    print('Fermat primality test')
    n = int(input('Enter number n you want check : '))
    t = int(input('Enter safety parameter t  :  '))
    print(Fermat(n,t))

