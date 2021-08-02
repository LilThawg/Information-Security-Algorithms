def prefix (pattern):
    arr = []
    for i in range(len(pattern)):
        arr.append(pattern[0:i+1])
    return arr

def suffix (pattern):
    arr = []
    for i in range(len(pattern)):
        arr.append(pattern[i:len(pattern)])
    return arr

def Failure_function (pattern):
    P = pattern
    Fx = dict()
    for j in range(len(P)):
        if j == 0 :
            Fx[j] = -1
        else :
            Prefix = prefix(P[0:j])
            Suffix = suffix(P[1:j])
            arr = list(set(Prefix) & set(Suffix))
            if len(arr) == 0:
                Fx[j] = 0
            else :
                max_len = max([len(i) for i in arr])
                Fx[j] = max_len
    return Fx

def KMP (pattern,text):
    F = Failure_function(pattern)
    i = 0
    j = 0
    m = len(pattern)
    n = len(text)
    check = 0
    arr = []
    i_new = 0
    j_new = 0
    while i < n :

        if text[i] == pattern[j] :
            check = 1
            arr.append(f'{text[i]} va {pattern[j]}')
            if j == m - 1 :
                index = i-j
                return arr,index
            else :
                i = i + 1
                j = j + 1

        else :
            arr.append(f'{text[i]} va {pattern[j]}')

            if check == 1 or j_new != 0:
                i = i - j
            i_new = i + j - F[j]

            j_new = F[j]
            if F[j] == -1 :
                j_new = 0
            j = j_new

            if j_new != 0 :
                i = i_new + j_new
            else :
                i = i_new

            check = 0
    return arr,-1


if __name__ == '__main__':
    P = input()
    T = input()
    arr,index = KMP(P,T)
    if index != -1:
        print(f'Su xuat hien cua mau "{P}" trong van ban "{T}" co vi tri bat dau la {index}')
    else:
        print(f'Mau "{P}" khong xuat hien trong van ban "{T}"')
    print(f'So phep lap la {len(arr)}:')
    for i in range(len(arr)):
        print(f"{i + 1}: {arr[i]}")
'''
Input:
abd
abcaab

Output:
Mau "abd" khong xuat hien trong van ban "abcaab"
So phep lap la 8:
1: a va a
2: b va b
3: c va d
4: c va a
5: a va a
6: a va b
7: a va a
8: b va b
Example 2
Input:
aba
abcaabacabaca

Output:
Su xuat hien cua mau "aba" trong van ban "abcaabacabaca" co vi tri bat dau la 4
So phep lap la 9:
1: a va a
2: b va b
3: c va a
4: c va a
5: a va a
6: a va b
7: a va a
8: b va b
9: a va a
'''
