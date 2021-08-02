#Tính nghịch đảo trên Fp dùng Euclide mở rộng
def GCD_extended(a, b):
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, b
	while v3 != 0:
		q = u3//v3
		t1, t2, t3 = u1 - q*v1, u2 - q*v2, u3 - q*v3
		u1, u2, u3 = v1, v2, v3
		v1, v2, v3 = t1, t2, t3
	return u1, u2, u3

def Extended_Euclide(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u!= 1:
        q = v//u
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1%p

if __name__ == '__main__':
    p = int(input())
    a = int(input())
    print(str(a) + "^-1 mod " + str(p) + " = " + str(Extended_Euclide(a,p)))
    
'''
Input:
489573857
45682375

Output:
45682375^-1 mod 489573857 = 242160691
'''

