import math
# trừ chính xác bội
# đầu vào là 2 arr, arr A - arr B, nếu đầu vào là 2 số thì chuyển 2 số sang arr rồi làm
def Multiprecision_subtraction(a, b, w=8, p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    c = [''] * t # khởi tạo arr c gồm t phần tử
    e = 0   # bit nhớ khởi tạo = 0
    # mô tả thuật toán :
        # làm từ cuối arr trở lên
        # c[i] = a[i] - b[i] - e (mod 2^8)
        # nếu a[i] - b[i] - e < 0 : e = 1
        # nếu không thì           : e = 0
    for i in range(t):
        c[t-1-i] = (a[t-1-i] - b[t-1-i] - e) % (2**w)
        if a[t-1-i] - b[t-1-i] - e < 0 :
            e = 1
        else :
            e = 0
    return e,c

if __name__ == '__main__':
    a = [57,169,36,27]
    b = [0,98,34,62]
    print(Multiprecision_subtraction(a,b))
