import math
#biểu diễn số A thành một arr
def number_to_array (a,w=8,p=2147483647):
    m = math.ceil(math.log(p, 2))  #m = làm tròn lên log cơ số 2 của p
    t = math.ceil(m / w) # với w bits, w là bội số của 8, t được tính = làm tròn lên (m / w)
    arr = ['']*t # khởi tạo arr gồm t phần tử
    tmp = a #khởi tạo tmp = a đóng vai trò như là phần dư sau mỗi lần tính toán
    for i in range(t):
        x = pow(2, ((t - 1 - i) * w))
        arr[i] = tmp // x
        tmp = tmp % (arr[i]*x)
    return arr

if __name__ == '__main__':
    print(number_to_array(2147483647))
