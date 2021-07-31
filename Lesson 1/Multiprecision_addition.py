import math
# cộng chính xác bội
# đầu vào là 2 arr nếu đầu vào là 2 số thì chuyển 2 số sang arr rồi làm
def Multiprecision_addition(a, b, w=8, p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    c = [''] * t # khởi tạo arr c gồm t phần tử
    e = 0 # bit nhớ khởi tạo = 0
    # mô tả thuật toán :
        # làm từ cuối arr trở lên
        # c[i] = a[i] + b[i] + e (mod 2^8)
        # nếu a[i] + b[i] + e >= 2^8 : e = 1
        # nếu không thì              : e = 0
    for i in range(t):
        c[t-1-i] = (a[t-1-i] + b[t-1-i] + e) % (2**w)
        if a[t-1-i] + b[t-1-i] + e >= 2**w :
            e = 1
        else :
            e = 0
    return e,c

if __name__ == '__main__':
    a = [157,0,173,23]
    b = [169,1,0,64]
    print(Multiprecision_addition(a,b))
