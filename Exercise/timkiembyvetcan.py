#Tìm kiếm mẫu theo thuật toán vét cạn
def brute_force(pattern,text):
    i = 0
    j = 0
    m = len(pattern)
    n = len(text)

    arr = []
    while i < n :

        if text[i] == pattern[j]:
            arr.append(f'{text[i]} va {pattern[j]}')
            if j == m - 1:
                index = i - j
                return arr, index
            else:
                i = i + 1
                j = j + 1

        else :
            arr.append(f'{text[i]} va {pattern[j]}')
            i = i - j
            i = i + 1
            j = 0
            if n - i < m :
                break
    return arr,-1

if __name__ == '__main__':
    P = input()
    T = input()
    arr,index = brute_force(P,T)
    if index != -1:
        print(f'Su xuat hien cua mau "{P}" trong van ban "{T}" co vi tri bat dau la {index}, so phep lap la {len(arr)}')
    else:
        print(f'Mau "{P}" khong xuat hien trong van ban "{T}", so phep lap la {len(arr)}')
'''
Input:
oan
an toan

Output:
Su xuat hien cua mau "oan" trong van ban "an toan" co vi tri bat dau la 4, so phep lap la 7
Example 2
Input:
oano
an toan

Output:
Mau "oano" khong xuat hien trong van ban "an toan", so phep lap la 4
'''
