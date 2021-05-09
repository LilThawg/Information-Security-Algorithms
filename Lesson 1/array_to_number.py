import math

def array_to_number(arr,w=8,p=2147483647):
    m = math.ceil(math.log(p, 2))
    t = math.ceil(m / w)
    a = 0
    for i in range(t):
        x = pow(2, ((t - 1 - i) * w))
        a += arr[i] * x
    return a

if __name__ == '__main__':
    print(array_to_number([1, 101, 236, 21]))
