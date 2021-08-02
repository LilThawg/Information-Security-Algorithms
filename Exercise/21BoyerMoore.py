def last_occurrence(pattern,text):
    Lx = dict()
    alphabet = ''.join(set(text))
    for letter in alphabet:
        Lx[letter] = pattern.rfind(letter)
    return Lx

def Boyer_Moore(pattern,text):
    Lx = last_occurrence(pattern,text)
    m = len(pattern)
    n = len(text)
    i = m - 1
    j = m - 1
    res = []
    while i < n :
        res.append(f"{text[i]} va {pattern[j]}")
        if text[i] == pattern[j] :
            if j == 0:
                return res, i
            else :
                i = i - 1
                j = j - 1
        else :
            i = i + m - min(j, 1+Lx[text[i]])
            j = m - 1

    return res, -1

if __name__ == '__main__':
    P = input()
    T = input()
    arr,index = Boyer_Moore(P,T)
    if index != -1 :
        print(f'Su xuat hien cua mau "{P}" trong van ban "{T}" co vi tri bat dau la {index}')
    else :
        print(f'Mau "{P}" khong xuat hien trong van ban "{T}"')
    print(f'So phep lap la {len(arr)}:')
    print("   T va P")
    for i in range(len(arr)):
        print(f"{i+1}: {arr[i]}")


'''
Input:
rith
a pattern matching

Output:
Mau "rith" khong xuat hien trong van ban "a pattern matching"
So phep lap la 6:
   T va P
1: a va h
2: r va h
3: m va h
4: h va h
5: c va t
6: g va h
Example 2
Input:
rithm
a pattern matching algorithm

Output:
Su xuat hien cua mau "rithm" trong van ban "a pattern matching algorithm" co vi tri bat dau la 23
So phep lap la 11:
   T va P
1: t va m
2: e va m
3: a va m
4: n va m
5: g va m
6: h va m
7: m va m
8: h va h
9: t va t
10: i va i
11: r va r
'''
