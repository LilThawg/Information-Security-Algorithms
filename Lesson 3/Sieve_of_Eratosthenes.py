import math


def Sieve_of_Eratosthenes (n):

    arr = {}
    for i in range(2,n+1):
        arr[i] = True

    for i in range(2, math.ceil(math.sqrt(n))):
        if arr[i]:
            for j in range(i*2,n+1,i):
                arr[j] = False

    print(arr)

    primes = [i for i in range(2,n+1) if arr[i]]
    return primes

if __name__ == '__main__':
    n = int(input("Enter n to print primes <= n :  "))
    print(Sieve_of_Eratosthenes(n))
