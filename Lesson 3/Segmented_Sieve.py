import math

def Sieve_of_Eratosthenes (n):

    arr = {}
    for i in range(2,n+1):
        arr[i] = True

    for i in range(2, math.ceil(math.sqrt(n))):
        if arr[i]:
            for j in range(i**2,n+1,i):
                arr[j] = False

    primes = [i for i in range(2,n+1) if arr[i]]
    return primes

def Segmented_Sieve (n):
    delta = math.floor(math.sqrt(n)) - 1
    primes = Sieve_of_Eratosthenes(delta + 1)
    low = delta + 2
    high = low + delta
    while low <= n :
        if high > n : high = n+1

        arr = {}
        for i in range(low, high):
            arr[i] = True

        m = math.floor(math.sqrt(high-1))

        p = Sieve_of_Eratosthenes(m)

        for i in p:
            for j in range(low,high):
                if j%i == 0 : arr[j] = False

        for i in range(low, high):
            if arr[i]:
                primes.append(i)

        print(arr)

        low = low + delta
        high = high + delta

    return primes
if __name__ == '__main__':
    n = 30
    print(Segmented_Sieve(n))

