# Tìm ước chung lớn nhất của hai số
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
if __name__ == '__main__':
       t = int(input())
       for i in range(t):
           a,b = map(int, input().split())
           print(gcd(a,b))


'''
Input:
2
420 429
134 550

Output:
3
2
'''
