#Tìm phân tích nguyên tố của một số theo vét cạn
def prime_factor(n):
    N = n
    arr = []

    while n%2 == 0 :
        arr.append(2)
        n = n // 2

    for i in range(3,n+1,2):
        while n%i == 0 :
            arr.append(i)
            n = n//i
    res = []
    my_dict = {i: arr.count(i) for i in arr}

    for i in my_dict:
        res.append(f'{i}^{my_dict[i]}')

    Res = str(res).strip("[]").replace("', '"," + ").strip("'")
    return Res

if __name__ == '__main__':
    n = int(input())
    print(f'n = {n} = {prime_factor(n)}')

'''
Input:
20

Output:
n = 20 = 2^2 + 5^1
'''
