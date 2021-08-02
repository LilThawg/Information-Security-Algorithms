#Kiểm tra tính nguyên tố của một số theo fermat
def Fermat(a,n):
    if pow(a,n-1,n) != 1 :
        print(f"Co so a={a}: Hop so")
        return 0
    else :
        print(f"Co so a={a}: Nguyen to")
        return 1

if __name__ == '__main__':
    n = int(input())
    t = int(input())
    Array = list(map(int, input().split(' ')[:t]))
    Result = []
    print(f"Kiem tra so nguyen n={n}:")
    for i in Array:
        Result.append(Fermat(i,n))

    Check = 1
    for i in Result:
        if i!=1 :
            Check = 0

    if Check == 0:
        print(f"{n} la hop so")
    else :
        print(f"{n} co the la nguyen to")

'''
Kiểm tra tính nguyên tố của một số
Input
Dòng 1: n - số nguyên lẻ >=3 cần kiểm tra
Dòng 2: t - số lượng testcase
Dòng 3: chứa t số nguyên a (2≤a≤n-2), các số cách nhau một vị trí
Output
t dòng, mỗi dòng in ra kết quả tương ứng về tính nguyên tố của số nguyên theo mẫu
Example 1
Input:
50
3
16 29 16
Output:
Kiem tra so nguyen n=50:
Co so a=16: Hop so
Co so a=29: Hop so
Co so a=16: Hop so
50 la hop so
Example 2
Input:
47
5
12 8 42 11 39
Output:
Kiem tra so nguyen n=47:
Co so a=12: Nguyen to
Co so a=8: Nguyen to
Co so a=42: Nguyen to
Co so a=11: Nguyen to
Co so a=39: Nguyen to
47 co the la nguyen to
'''
