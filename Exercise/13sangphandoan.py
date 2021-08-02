import math
#Tìm các số nguyên tố theo sàng phân đoạn
def Segmented_Sieve (n,m):
    print(f"Chia pham vi tu 2 den {n} thanh cac doan co kich co {m}")

    x =[]
    start = 2
    while start <= n:
        end = start+m
        if end>n: end = n+1
        arr = [i for i in range(start,end)]
        x.append(arr)
        start = end
    for i in x :
        s = str(i).strip("[]").replace(", ","  ")
        if i != x[-1]: print(s,end="  ||")
        else : print(s)

    print("Xet doan 1:")
    start = 2
    end = start + m
    if end>n: end = n+1
    arr = {}
    for i in range(start,end):
        arr[i] = True
    for i in range(start,end):
        if arr[i]:
            for j in range(i*2,end,i):
                arr[j] = False
            print(f"p={i}")
            primes = [i for i in range(start,end) if arr[i]]
            print(str(primes).strip('[]').replace(", ", "  ") + "  ")

    for i in range(2,math.ceil((n-2+1)/m)+1):
        print(f"Xet doan {i}:")
        M = math.floor(math.sqrt(max(x[i-1])))
        for j in x[i-1] :
            arr[j] = True
        for p in [k for k in range(2,M+1) if arr[k]]:
            for j in x[i - 1]:
                if j % p == 0 : arr[j] = False
            print(f"p={p}")
            primes = [j for j in x[i - 1] if arr[j]]
            print(str(primes).strip('[]').replace(", ", "  ") + "  ")

    print(f"Tat ca cac so nguyen to <= {n}:")
    PRIMES = [i for i in range(2,n+1) if arr[i]]
    print(str(PRIMES).strip('[]').replace(", ", "  ") + " ")



if __name__ == '__main__':
    n,m = map(int, input().split())
    Segmented_Sieve(n,m)
'''
Input:
10 3

Output:
Chia pham vi tu 2 den 10 thanh cac doan co kich co 3
2  3  4  ||5  6  7  ||8  9  10
Xet doan 1:
p=2
2  3  
p=3
2  3  
Xet doan 2:
p=2
5  7  
Xet doan 3:
p=2
9  
p=3

Tat ca cac so nguyen to <= 10:
2  3  5  7 
'''
