#Tìm các số nguyên tố theo sàng nguyên thủy
def Sieve_of_Eratosthenes (n):

    arr = {}
    for i in range(2,n+1):
        arr[i] = True

    for i in range(2, n+1):
        if arr[i]:
            for j in range(i*2,n+1,i):
                arr[j] = False
            print(f"p={i}")
            primes = [i for i in range(2,n+1) if arr[i]]
            print(str(primes).strip('[]').replace(", ", "  ") + "  ")

    print(f"Cac so nguyen to <={n} la:")
    primes = [i for i in range(2, n + 1) if arr[i]]
    print(str(primes).strip('[]').replace(", ", "  ") + " ")


if __name__ == '__main__':
    n = int(input())
    print(f"Liet ke cac so nguyen tu 2 den {n}")
    print(str([i for i in range(2,n+1)]).strip('[]').replace(", ", "  "))
    Sieve_of_Eratosthenes(n)
'''
Input:
7

Output:
Liet ke cac so nguyen tu 2 den 7
2  3  4  5  6  7
p=2
2  3  5  7    
p=3
2  3  5  7  
p=5
2  3  5  7  
p=7
2  3  5  7  
Cac so nguyen to <=7 la:
2  3  5  7 
'''
