import math

def solve (w,p,a):
    m = math.ceil(math.log(p,2))
    t = math.ceil(m/w)
    arr = []
    for i in range(t,0,-1):
        arr.append(pow(2,(i-1)*w))
    ARR = []
    sum = 0
    tmp = a
    for j in range(t):
        coefficient = tmp // arr[j]
        ARR.append(coefficient)
        sum+= coefficient*arr[j]
        tmp = a - sum
    print(ARR)

if __name__ == '__main__':
    w = int(input("Please enter w-bit(w is multiple of 8), w = "))
    p = int(input("p = "))
    a = int(input("a = "))
    solve(w,p,a)
