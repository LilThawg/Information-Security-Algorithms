import math
#biểu diễn ma trận A thành số
def array_to_number(arr,w=8,p=2147483647):
    m = math.ceil(math.log(p, 2)) #m = làm tròn lên log cơ số 2 của p
    t = math.ceil(m / w) # với w bits, w là bội số của 8, t được tính = làm tròn lên (m / w)
    sum = 0
    for i in range(t):
        x = pow(2, ((t - 1 - i) * w))
        sum += arr[i] * x
    return sum

if __name__ == '__main__':
    print(array_to_number([127, 255, 255, 255]))
