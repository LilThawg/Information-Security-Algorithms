def find_s_r(n):
    s = 1
    while True:
        if (n-1)%(2**s) != 0:
            break
        s+=1
    s = s-1
    r = (n-1)//(2**s)
    return s,r

def Miler_Rabin(n,a,b):
    s, r = find_s_r(n)
    print(f'Kiem tra so nguyen n={n}:')
    print(f'{n}-1 = 2^{s}.{r}')
    check = []
    for i in range(a+1,b):
        res = True
        a = i
        print(f'Co so a= {a}:')
        y = pow(a,r,n)

        if y != 1 and y != n-1:
            print(f'y= {y} => (y!=1)&&(y!=n-1)')
            j = 1
            print(" "*3 + "j=1")
            print(" "*3 + f'j=1, y={y} =>(j<=s-1)&&(y!=n-1)')

            while j <= s - 1 and y != n - 1:
                y = pow(y,2,n)
                j = j + 1
                if j <= s - 1 :
                    if y == 1 :
                        print(" "*3+f'y={y}')
                        print('Ket qua: Hop so')
                        res = False
                        break
                    print(" " * 3 + f'j={j}, y={y} =>(j<=s-1)&&(y!=n-1)')
            if y != n - 1 and j > s - 1:
                if y == 1 :
                    print(" "*3+f'y={y}')
                else :
                    print(f'y = {y} => y!=n-1')
                print('Ket qua: Hop so')
                res = False

        else :
            print('Ket qua: Nguyen to')

        check.append(res)
    if all(check) :
        return f'{n} co the la nguyen to'
    else :
        return f'{n} la hop so'

if __name__ == '__main__':
    n = int(input())
    a,b = map(int, input().split())
    print(Miler_Rabin(n,a,b))

'''
Input:
5
2 5

Output:
Kiem tra so nguyen n=5:
5-1 = 2^2.1
Co so a= 3:
y= 3 => (y!=1)&&(y!=n-1)
   j=1
   j=1, y=3 =>(j<=s-1)&&(y!=n-1)
Ket qua: Nguyen to
Co so a= 4:
Ket qua: Nguyen to
5 co the la nguyen to
Example 2
Input:
9
2 5

Output:
Kiem tra so nguyen n=9:
9-1 = 2^3.1
Co so a= 3:
y= 3 => (y!=1)&&(y!=n-1)
   j=1
   j=1, y=3 =>(j<=s-1)&&(y!=n-1)
   j=2, y=0 =>(j<=s-1)&&(y!=n-1)
y = 0 => y!=n-1
Ket qua: Hop so
Co so a= 4:
y= 4 => (y!=1)&&(y!=n-1)
   j=1
   j=1, y=4 =>(j<=s-1)&&(y!=n-1)
   j=2, y=7 =>(j<=s-1)&&(y!=n-1)
y = 4 => y!=n-1
Ket qua: Hop so
9 la hop so
'''
