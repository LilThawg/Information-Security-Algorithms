#Tìm một thừa số không tầm thường của một số
import math
#if result wrong, please change c != 1 , example : x**2 + 9 instead of c = 1 or anything
def Pollard_Rho(n , seed = 2 , f = lambda x: x**2 + 1):
    a = seed
    b = seed
    arr = []
    while 1:
        a = f(a) % n
        b = f(f(b) %n) % n
        d = math.gcd(abs(a-b),n)
        arr.append([a,b,d])
        if 1 < d and d < n :
            break
        elif d == n :
            break

    print("""----------------------------------------------------------------
|                   a|                   b|                   d|
----------------------------------------------------------------""")
    for i in range(len(arr)):
        a,b,d = arr[i]
        print("|"+" "*(20-len(str(a)))+str(a)+"|"+" "*(20-len(str(b)))+str(b)+"|"+" "*(20-len(str(d)))+str(d)+"|")
        print("----------------------------------------------------------------")

    if d == n : print("Khong tim thay")
    else : print(f"Thua so khong tam thuong cua {n} la {d}")

if __name__ == '__main__':
    n = int(input())
    Pollard_Rho(n)


'''
Input:
65

Output:
----------------------------------------------------------------
|                   a|                   b|                   d|
----------------------------------------------------------------
|                   5|                  26|                   1|
----------------------------------------------------------------
|                  26|                  15|                   1|
----------------------------------------------------------------
|                  27|                  52|                   5|
----------------------------------------------------------------
Thua so khong tam thuong cua 65 la 5
'''
