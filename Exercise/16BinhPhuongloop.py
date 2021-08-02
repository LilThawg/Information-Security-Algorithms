def squared_algorithm_with_iterative (a,k,n):
    print(f"Chuyen {k} sang nhi phan: {bin(k)[2:]}")
    k = bin(k)[2:][::-1]
    k = list(k)
    t = len(k)
    b = 1
    A = a
    print(f"Dat A=a={A}")
    if k[0] == '1':
        b = a
        print(f"- k_0=1, dat b=a={a}")
    for i in range(1,t):
        A = A*A % n
        print(f"Dat A=A^2 mod {n}={A}")
        if k[i] == '1':
            b = A*b % n
            print(f"- k_{i} =1, dat b=b*A mod {n}={b}")
    return b

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    k = int(input())
    print(f"=> {a}^{k} mod {n}={squared_algorithm_with_iterative(a,k,n)}")

'''
Input:
1234
5
596

Output:
Chuyen 596 sang nhi phan: 1001010100
Dat A=a=5
Dat A=A^2 mod 1234=25
Dat A=A^2 mod 1234=625
- k_2 =1, dat b=b*A mod 1234=625
Dat A=A^2 mod 1234=681
Dat A=A^2 mod 1234=1011
- k_4 =1, dat b=b*A mod 1234=67
Dat A=A^2 mod 1234=369
Dat A=A^2 mod 1234=421
- k_6 =1, dat b=b*A mod 1234=1059
Dat A=A^2 mod 1234=779
Dat A=A^2 mod 1234=947
Dat A=A^2 mod 1234=925
- k_9 =1, dat b=b*A mod 1234=1013
=> 5^596 mod 1234=1013
'''
